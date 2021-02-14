import re

from django import forms

from apps.users.models import User
from .base import BaseRegisterForm


class SellerRegisterForm(BaseRegisterForm):
    ERROR_MESSAGES = {
        'password_mismatch': "رمز عبور وارد شده با تکرار رمز عبور مغایرت دارد",
    }

    LEGAL_CHOICES = (
        (User.LEGAL_INDIVIDUAL, 'حقیقی',),
        (User.LEGAL_LEGAL, 'حقوقی',),
    )

    LOCATION_CHOICES = (
        ('tehran', 'تهران',),
        ('not-tehran', 'شهرستان',),
    )

    legal_type = forms.ChoiceField(label="Legal Type", choices=LEGAL_CHOICES, required=True)
    username = forms.CharField(min_length=4, max_length=255, required=False)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput, required=True)
    full_name = forms.CharField(label="Full Name", required=True)
    id_code = forms.CharField(label="ID Code", required=True)
    phone_number = forms.CharField(label="Phone Number", required=True)
    mobile_number = forms.CharField(label="Mobile Number", required=False)
    fax_number = forms.CharField(label="Fax Number", required=False)
    email = forms.EmailField(label="Email", required=False)
    region = forms.ChoiceField(label="Region", choices=LOCATION_CHOICES, required=True)
    address = forms.CharField(label="Address", required=True)
    postal_code = forms.CharField(label="Postal Code", required=True)

    class Meta:
        model = User
        fields = ('use_type', 'legal_type', 'username', 'full_name', 'id_code', 'phone_number', 'password1',
                  'password2', 'mobile_number', 'fax_number', 'email', 'region', 'address', 'postal_code',)

    def clean_email(self):
        email = self.cleaned_data['email'].lower().strip()
        if not re.match(r"^\S+@\S+\.\S+$", email):
            raise forms.ValidationError("لطفا ایمیل خود را با فرمت درست وارد نمایید")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name'].lower().strip()
        return full_name

    def clean_id_code(self):
        id_code = self.cleaned_data['id_code'].lower().strip()
        return id_code

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        phone_number.replace("-", "").replace(" ", "")
        if not phone_number.isdigit():
            raise forms.ValidationError("لطفا شماره تلفن خود را بصورت عددی وارد نمایید")
        if not re.match(r"0\d{8,12}", phone_number):
            raise forms.ValidationError("شماره تلفن باید بین ۹ تا ۱۳ رقم باشد و کد شهر وارد شود")
        return phone_number

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        mobile_number.replace("-", "").replace(" ", "")
        if not mobile_number.isdigit():
            raise forms.ValidationError("لطفا شماره موبایل خود را بصورت عددی وارد نمایید")
        if not re.match(r"0\d{10}", mobile_number):
            raise forms.ValidationError("شماره موبایل باید ۱۱ رقم باشد و با 0 شروع شود")
        return mobile_number

    def clean_fax_number(self):
        fax_number = self.cleaned_data['fax_number']
        fax_number.replace("-", "").replace(" ", "")
        if not fax_number.isdigit():
            raise ValueError("لطفا شماره فکس خود را بصورت عددی وارد نمایید")
        if not re.match(r"0\d{8,12}", fax_number):
            raise ValueError("شماره فکس باید بین ۹ تا ۱۳ رقم باشد و کد شهر وارد شود")
        return fax_number

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.ERROR_MESSAGES['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean_address(self):
        # TODO: Validate Address
        address = self.cleaned_data['address'].lower().strip()
        return address

    def clean_postal_code(self):
        # TODO: Validate Postal Code
        postal_code = self.cleaned_data['postal_code'].lower().strip()
        return postal_code

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
