from django import forms

from apps.products.models import Product


class AddProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    ERROR_MESSAGES = {
        'password_mismatch': "رمز عبور وارد شده با تکرار رمز عبور مغایرت دارد",
    }

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
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
