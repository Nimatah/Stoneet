from django import forms

from apps.products.models import Product


class AddProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    category = forms.CharField(label="Category", required=True)
    title = forms.CharField(label="Title", required=True)
    location = forms.CharField(label="Location", required=False)
    description = forms.CharField(label="Description", required=True)
    user = forms.CharField(label="User", required=True)

    class Meta:
        model = Product
        fields = ('category', 'title', 'location', 'description', )
        exclude = ('user',)

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
        return product
