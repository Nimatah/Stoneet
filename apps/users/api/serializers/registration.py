import re

from rest_framework import serializers

from apps.users.models import User


class RegistrationAuthValidationSerializer(serializers.Serializer):

    email = serializers.CharField(required=True, label='ایمیل', write_only=True)
    password = serializers.CharField(required=True, label='رمز عبور', write_only=True)
    mobile_number = serializers.CharField(required=True, label='شماره موبایل', write_only=True)

    def validate_email(self, value: str) -> str:
        value = value.strip().lower()
        if not re.match(r'^\S+@\S+\.\S+$', value):
            raise serializers.ValidationError('لطفا ایمیل را با فرمت صحیح وارد کنید.')
        return value

    def validate_password(self, value: str) -> str:
        if 8 > len(value) > 50:
            raise serializers.ValidationError('رمز عبور باید بیشتر از ۸ کاراکتر باشد.')
        return value

    def validate_mobile_number(self, value: str) -> str:
        value = value.strip()
        try:
            int(value)
            if len(value) != 11:
                raise serializers.ValidationError('شماره موبایل باید ۱۱ رقم باشد')
        except ValueError:
            raise serializers.ValidationError('شماره موبایل رو به صورت عددی وارد نمایید')
        return value

    def validate(self, attrs):
        user = User.objects.find_by_email_or_phone_number(attrs['email'], attrs['mobile_number'])
        if user is None:
            return attrs
        if user.mobile_number == attrs['mobile_number']:
            raise serializers.ValidationError('کاربر با شماره تلفن وارد شده قبلا ایجاد شده است')
        if user.email == attrs['email']:
            raise serializers.ValidationError('کاربر با ایمیل واره شده قبلا ایجاد شده است')
        return attrs
