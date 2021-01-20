from typing import List

from django import forms
from django.db import transaction

from apps.products.models import (
    Product,
    Category,
    Attribute,
    ProductMedia,
    ProductAttribute,
    AttributeMedia,
)


class CreateProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    category = forms.CharField(label="Category", required=True)
    title = forms.CharField(label="Title", required=True)
    description = forms.CharField(label="Description", required=False, widget=forms.Textarea)
    attributes = forms.Field(required=False)
    analyze = forms.ImageField(required=True)
    image_primary = forms.ImageField(required=True)
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    user = forms.CharField(label="User", required=False)

    class Meta:
        model = Product
        fields = ('category', 'title', 'attributes', 'description', 'analyze',
                  'image_primary', 'image1', 'image2', 'image3', 'image4',)
        exclude = ('user', 'attributes',)

    def clean(self):
        attributes = []
        for k, v in self.data.items():
            if k.startswith('attribute-'):
                key = k.replace('attribute-', '')
                attr = Attribute.objects.get(pk=key)
                if attr.is_valid(v):
                    value = v
                else:
                    raise forms.ValidationError(f"incorrect value {key} {v}")
                attributes.append({'attr': attr, 'value': value})

        self.cleaned_data['attributes'] = attributes
        return super().clean()

    def clean_category(self):
        try:
            return Category.objects.get(pk=self.cleaned_data['category'])
        except Category.DoesNotExist:
            raise forms.ValidationError("گروه پیدا نشد")

    def save(self, commit=True):
        product = Product()
        product.category = self.cleaned_data['category']
        product.title = self.cleaned_data['title']
        product.description = self.cleaned_data['description']
        product.user = self.user

        images = self.handle_product_images(product)

        if commit:
            with transaction.atomic():
                product.save()
                for image in images:
                    image.save()
                self.handle_analyze(product)
                for i in self.cleaned_data['attributes']:
                    product_attribute = ProductAttribute()
                    product_attribute.product = product
                    product_attribute.attribute = i['attr']
                    product_attribute.value = i['value']
                    product_attribute.save()
        return product

    def handle_product_images(self, product: Product) -> List[ProductMedia]:
        images: List[ProductMedia] = []
        for k, v in self.cleaned_data.items():
            if not k.startswith('image'):
                continue
            image = ProductMedia()
            image.type = ProductMedia.TYPE_IMAGE
            image.file = v
            image.product = product
            if k == 'image_primary':
                image.is_primary = True
            images.append(image)
        return images

    def handle_analyze(self, product: Product) -> None:
        product_attribute = ProductAttribute.objects.create(attribute_id=Attribute.ID_ANALYZE, product=product)
        AttributeMedia.objects.create(
            type=AttributeMedia.TYPE_IMAGE,
            product_attribute=product_attribute,
            file=self.cleaned_data['analyze'],
        )
