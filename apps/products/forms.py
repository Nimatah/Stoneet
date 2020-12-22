from django import forms

from apps.products.models import Product, Category, Attribute, ProductMedia, ProductAttribute


class AddProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    category = forms.CharField(label="Category", required=True)
    title = forms.CharField(label="Title", required=True)
    attributes = forms.Field(required=False)
    description = forms.CharField(label="Description", required=True, widget=forms.Textarea)
    image = forms.ImageField()
    user = forms.CharField(label="User", required=False)

    class Meta:
        model = Product
        fields = ('category', 'title', 'attributes', 'description', 'image',)
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
        print(self.cleaned_data)
        product = Product()
        product.category = self.cleaned_data['category']
        product.title = self.cleaned_data['title']
        product.description = self.cleaned_data['description']
        product.user = self.user

        media = ProductMedia()
        media.type = ProductMedia.TYPE_IMAGE
        media.file = self.cleaned_data['image']
        media.product = product

        if commit:
            product.save()
            media.save()
            for i in self.cleaned_data['attributes']:
                product_attribute = ProductAttribute()
                product_attribute.product = product
                product_attribute.attribute = i['attr']
                product_attribute.value = i['value']
                print(product_attribute.__dict__)
                product_attribute.save()
        return product
