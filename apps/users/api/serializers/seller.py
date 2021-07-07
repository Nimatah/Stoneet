from rest_framework import serializers

from apps.products.models import Attribute
from apps.users.models import Mine


class SellerAddProductPart1ValidationSerializer(serializers.Serializer):

    attribute_1 = serializers.IntegerField(required=True, label='قیمت')  # Price
    weight_attribute_1 = serializers.CharField(required=True, label='واحد قیمت')
    attribute_4 = serializers.IntegerField(required=True, label='ظرفیت تامین ماهانه')  # SKU
    attribute_5 = serializers.IntegerField(required=False, label='ارسال نمونه')  # Sample
    attribute_9 = serializers.CharField(required=True, label='شرایط پرداخت وجه')  # Payment
    attribute_12 = serializers.IntegerField(required=True, label='عیار کمترین')  # Caret From
    attribute_13 = serializers.IntegerField(required=True, label='عیار بیشترین')  # Caret To
    attribute_14 = serializers.IntegerField(required=True, label='دانه بندی کمترین')  # Grain From
    attribute_15 = serializers.IntegerField(required=True, label='دانه بندی بیشترین')  # Grain To
    attribute_16 = serializers.CharField(required=True, label='نحوه ارسال')  # Delivery Type
    child_attribute_16 = serializers.IntegerField(required=False, label='مقدار نحوه ارسال')  # Delivery Type
    weight_attribute_16 = serializers.CharField(required=False, label='واحد مقدار نحوه ارسال')  # Delivery Type
    attribute_17 = serializers.FloatField(required=True, label='میزان دپوی موجود')
    attribute_18 = serializers.IntegerField(required=True, label='حداقل میزان سفارش')
    mine = serializers.IntegerField(required=False, label='معدن', allow_null=True)

    def validate_attribute_1(self, value):
        if value <= 0:
            raise serializers.ValidationError("قیمت نمیتواند صفر یا کمتر باشد")
        return value

    def validate_attribute_4(self, value):
        if value <= 0:
            raise serializers.ValidationError("ظرفیت تامین ماهانه نمیتواند صفر یا کمتر باشد")
        return value

    def validate_attribute_5(self, value):
        if value <= 0:
            raise serializers.ValidationError("مقدار ارسال نمونه نمیتواند صفر یا کمتر باشد")
        return value

    def validate_attribute_9(self, value):
        for v in value.split('|'):
            if v not in Attribute.objects.get(pk=Attribute.ID_PAYMENT_TYPE).choices:
                raise serializers.ValidationError("نحوه پرداخت باید نقدی، اقساطی یا هردو باشد")
        return value

    def validate_attribute_12(self, value):
        if value <= 0:
            raise serializers.ValidationError("عیار نمیتواند صفر یا کمتر باشد")
        if value > 100:
            raise serializers.ValidationError("عیار نمیتواند بیشتر از صد باشد")
        return value

    def validate_attribute_13(self, value):
        if value <= 0:
            raise serializers.ValidationError("عیار نمیتواند صفر یا کمتر باشد")
        if value > 100:
            raise serializers.ValidationError("عیار نمیتواند بیشتر از صد باشد")
        return value

    def validate_attribute_14(self, value):
        if value >= 100000:
            raise serializers.ValidationError("دانه بندی نمیتواند از صد هزار بیشتر باشد")
        return value

    def validate_attribute_15(self, value):
        if value >= 100000:
            raise serializers.ValidationError("دانه بندی نمیتواند از صد هزار بیشتر باشد")
        return value

    def validate_attribute_16(self, value):
        if value not in Attribute.objects.get(pk=Attribute.ID_DELIVERY_TYPE).choices:
            raise serializers.ValidationError("نوع تحویل غیر مجاز است")
        return value

    def validate_child_attribute_16(self, value):
        if value < 0:
            raise serializers.ValidationError("مقدار نوع تحویل نمیتواند کمتر از صفر باشد")
        return value

    def validate_weight_attribute_16(self, value):
        if value not in (Attribute.WEIGHT_KG, Attribute.WEIGHT_TON, 'default'):
            raise serializers.ValidationError("واحد مقدار نوع تحویل باید کیلوگرم یا تن باشد")
        return value

    def validate_weight_attribute_1(self, value):
        if value not in (Attribute.WEIGHT_KG, Attribute.WEIGHT_TON):
            raise serializers.ValidationError("واحد قیمت باید به ازای کیلوگرم یا تن باشد")
        return value

    def validate_mine(self, value):
        try:
            Mine.objects.get(pk=value)
        except Mine.DoesNotExist:
            raise serializers.ValidationError('لطفا ابتدا معدن را از پروفایل بسازید')
        return value
