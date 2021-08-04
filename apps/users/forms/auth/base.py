import re

from django import forms
from django.conf import settings

from apps.users.models import User


class BaseUserRegisterForm(forms.Form):
    ERROR_MESSAGES = {
        'password_mismatch': "رمز عبور وارد شده با تکرار رمز عبور مغایرت دارد",
    }

    LEGAL_CHOICES = (
        (User.LEGAL_INDIVIDUAL, 'حقیقی',),
        (User.LEGAL_LEGAL, 'حقوقی',),
    )

    legal_type = forms.ChoiceField(label="Legal Type", choices=LEGAL_CHOICES, required=True)
    username = forms.CharField(min_length=4, max_length=255, required=False)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    email = forms.EmailField(label="Email", required=False)
    mobile_number = forms.CharField(label="Mobile Number", required=False)

    def clean_email(self):
        email = self.cleaned_data['email'].lower().strip()
        if not re.match(r"^\S+@\S+\.\S+$", email):
            raise forms.ValidationError("لطفا ایمیل خود را با فرمت درست وارد نمایید")
        return email

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        mobile_number.replace("-", "").replace(" ", "")
        if not mobile_number.isdigit():
            raise forms.ValidationError("لطفا شماره موبایل خود را بصورت عددی وارد نمایید")
        if not re.match(r"0\d{10}", mobile_number):
            raise forms.ValidationError("شماره موبایل باید ۱۱ رقم باشد و با 0 شروع شود")
        return mobile_number

    @staticmethod
    def _file_size_valid(file):
        return file._size <= settings.MAX_UPLOAD_SIZE
