import re
from typing import List
from datetime import date

from django import forms
from django.db import transaction
from persiantools import jdatetime

from apps.users.models import User, UserMedia, Profile
from apps.locations.models import Region
from .base import BaseUserRegisterForm


class SellerRegisterForm(BaseUserRegisterForm):
    ERROR_MESSAGES = {
        'password_mismatch': "رمز عبور وارد شده با تکرار رمز عبور مغایرت دارد",
    }

    use_type = forms.CharField(label="User Type", initial=User.TYPE_SELLER, required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    birthday = forms.CharField(required=False)
    gender = forms.CharField(required=False)
    id_code = forms.CharField(required=False)
    national_code = forms.CharField(required=False)

    address = forms.CharField(required=False)
    postal_code = forms.CharField(required=False)
    region = forms.IntegerField(required=False)
    phone_number = forms.CharField(required=False)
    bank_account_name = forms.CharField(required=False)
    bank_account_number = forms.CharField(required=False)
    bank_sheba_number = forms.CharField(required=False)

    company_name = forms.CharField(required=False)
    company_type = forms.CharField(required=False)
    company_register_code = forms.CharField(required=False)
    company_national_code = forms.CharField(required=False)
    company_finance_code = forms.CharField(required=False)
    company_print_signature_right = forms.CharField(required=False)

    image_id_card_front = forms.ImageField(required=False)
    image_id_card_back = forms.ImageField(required=False)

    image_company_registration = forms.ImageField(required=False)
    image_company_latest_newspaper = forms.ImageField(required=False)
    image_company_tax_on_added_value_certificate = forms.ImageField(required=False)

    class Meta:
        fields = ('first_name', 'last_name', 'birthday', 'gender', 'id_code', 'national_code',
                  'address', 'postal_code', 'region', 'phone_number', 'bank_account_name',
                  'bank_sheba_number', 'company_name', 'company_type', 'company_register_code',
                  'company_national_code', 'company_finance_code', 'company_print_signature_right',
                  'image_id_card_front', 'image_id_card_back', 'image_company_registration',
                  'image_company_latest_newspaper', 'image_company_tax_on_added_value_certificate')

    def clean_use_type(self) -> str:
        value = User.TYPE_BUYER
        return value

    def clean_first_name(self) -> str:
        if not self.cleaned_data['first_name']:
            return ''
        return self.cleaned_data['first_name'].strip().lower()

    def clean_last_name(self) -> str:
        if not self.cleaned_data['last_name']:
            return ''
        return self.cleaned_data['last_name'].strip().lower()

    def clean_birthday(self) -> date:
        if not self.cleaned_data['birthday']:
            return date.today()
        value = self.cleaned_data['birthday'].strip().lower()
        if not re.match(r'\d{4}-\d{2}-\d{2}', value):
            raise forms.ValidationError('فرمت تاریخ تولد غلط است')
        return jdatetime.JalaliDate(*map(lambda x: int(x), value.split('-'))).to_gregorian()

    def clean_gender(self) -> str:
        if not self.cleaned_data['gender']:
            return ''
        if self.cleaned_data['gender'] not in (Profile.GENDER_MALE, Profile.GENDER_FEMALE,):
            raise forms.ValidationError('جنسیت باید مرد یا زن باشد')
        return self.cleaned_data['gender']

    def clean_id_code(self) -> str:
        if not self.cleaned_data['id_code']:
            return ''
        return self.cleaned_data['id_code'].strip().lower()

    def clean_national_code(self) -> str:
        if not self.cleaned_data['national_code']:
            return ''
        return self.cleaned_data['national_code'].strip().lower()

    def clean_address(self) -> str:
        if not self.cleaned_data['address']:
            return ''
        return self.cleaned_data['address'].strip().lower()

    def clean_postal_code(self) -> str:
        return self.cleaned_data['postal_code'].strip().lower()

    def clean_region(self) -> str:
        value = self.cleaned_data['region']
        if not Region.objects.filter(pk=value).exists():
            raise forms.ValidationError('شهر به درستی وارد نشده')
        return value

    def clean_phone_number(self) -> str:
        try:
            int(self.cleaned_data['phone_number'])
        except ValueError:
            raise forms.ValidationError('شماره تلفن به درستی وارد نشده')
        return self.cleaned_data['phone_number']

    def clean_bank_account_name(self) -> str:
        return self.cleaned_data['bank_account_name'].strip().lower()

    def clean_bank_sheba_number(self) -> str:
        return self.cleaned_data['bank_sheba_number'].strip().lower()

    def clean_company_name(self) -> str:
        if not self.cleaned_data['company_name']:
            return ''
        return self.cleaned_data['company_name'].strip().lower()

    def clean_company_register_code(self) -> str:
        if not self.cleaned_data['company_register_code']:
            return ''
        return self.cleaned_data['company_register_code'].strip().lower()

    def clean_company_national_code(self) -> str:
        if not self.cleaned_data['company_national_code']:
            return ''
        return self.cleaned_data['company_national_code'].strip().lower()

    def clean_company_finance_code(self) -> str:
        if not self.cleaned_data['company_finance_code']:
            return ''
        return self.cleaned_data['company_finance_code'].strip().lower()

    def clean_company_print_signature_right(self) -> str:
        if not self.cleaned_data['company_print_signature_right']:
            return ''
        return self.cleaned_data['company_print_signature_right'].strip().lower()

    def save(self, commit: bool = True) -> User:
        with transaction.atomic():
            user = User.objects.create(
                use_type=self.cleaned_data['use_type'],
                username=self.cleaned_data['email'],
                mobile_number=self.cleaned_data['mobile_number'],
                email=self.cleaned_data['email'],
            )
            user.set_password(self.cleaned_data['password'])
            images = self._handle_images(user)
            if commit:
                user.save()
                user.profile = self._create_individual_profile() \
                    if self.cleaned_data['legal_type'] == User.LEGAL_INDIVIDUAL \
                    else self._create_legal_profile()
                user.profile.save()
                for i in images:
                    i.save()
            return user

    def _create_individual_profile(self) -> Profile:
        profile = Profile()
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.birthday = self.cleaned_data['birthday']
        profile.gender = self.cleaned_data['gender']
        profile.id_code = self.cleaned_data['id_code']
        profile.national_code = self.cleaned_data['national_code']
        profile.address = self.cleaned_data['address']
        profile.postal_code = self.cleaned_data['postal_code']
        profile.region_id = self.cleaned_data['region']
        profile.phone_number = self.cleaned_data['phone_number']
        profile.bank_account_name = self.cleaned_data['bank_account_name']
        profile.bank_account_number = self.cleaned_data['bank_account_number']
        profile.bank_sheba_number = self.cleaned_data['bank_sheba_number']
        return profile

    def _create_legal_profile(self) -> Profile:
        profile = Profile()
        profile.address = self.cleaned_data['address']
        profile.postal_code = self.cleaned_data['postal_code']
        profile.region_id = self.cleaned_data['region']
        profile.phone_number = self.cleaned_data['phone_number']
        profile.bank_account_name = self.cleaned_data['bank_account_name']
        profile.bank_account_number = self.cleaned_data['bank_account_number']
        profile.bank_sheba_number = self.cleaned_data['bank_sheba_number']
        profile.company_name = self.cleaned_data['company_name']
        profile.company_type = self.cleaned_data['company_type']
        profile.company_register_code = self.cleaned_data['company_register_code']
        profile.company_national_code = self.cleaned_data['company_national_code']
        profile.company_finance_code = self.cleaned_data['company_finance_code']
        profile.company_print_signature_right = self.cleaned_data['company_print_signature_right']
        return profile

    def _handle_images(self, user: User) -> List[UserMedia]:
        images: List[UserMedia] = []
        for k, v in self.cleaned_data.items():
            if not k.startswith('image_'):
                continue
            if not v:
                continue
            image = UserMedia(
                user=user,
                title=UserMedia.name_map[k],
                file=v,
                type=UserMedia.TYPE_IMAGE,
            )
            images.append(image)
        return images
