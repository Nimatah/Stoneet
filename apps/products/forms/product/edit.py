from django import forms
from django.db import transaction

from apps.products.models import Product, Attribute, ProductMedia, ProductAttribute


class EditProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    title = forms.CharField(label="Title", required=True)
    attributes = forms.Field(required=False)
    description = forms.CharField(label="Description", required=True, widget=forms.Textarea)
    image = forms.ImageField(required=False)
    user = forms.CharField(label="User", required=False)

    class Meta:
        model = Product
        fields = ('title', 'attributes', 'description', 'image',)
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

    def save(self, commit=True):
        self.instance.title = self.cleaned_data['title']
        self.instance.description = self.cleaned_data['description']

        media = ProductMedia()
        media.type = ProductMedia.TYPE_IMAGE
        media.file = self.cleaned_data['image']
        media.product = self.instance

        if commit:
            with transaction.atomic():
                self.instance.save()

                self.instance.media.all().delete()
                media.save()

                self.instance.attributes.all().delete()
                for i in self.cleaned_data['attributes']:
                    product_attribute = ProductAttribute()
                    product_attribute.product = self.instance
                    product_attribute.attribute = i['attr']
                    product_attribute.value = i['value']
                    product_attribute.save()
        return self.instance
