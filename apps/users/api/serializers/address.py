from rest_framework import serializers

from apps.users.models import User, Address
from apps.locations.models import Region


class AddressSerializer(serializers.ModelSerializer):

    receiver_name = serializers.CharField(label='نام تحویل گیرنده')
    region_id = serializers.IntegerField(label='شهر')
    address = serializers.CharField(label='آدرس')
    postal_code = serializers.CharField(label='کد پستی')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = ('receiver_name', 'region_id', 'user', 'address', 'postal_code',)

    def validate_receiver_name(self, value: str) -> str:
        return value.strip().lower()

    def validate_region_id(self, value: int) -> int:
        try:
            Region.objects.get(pk=value)
        except Region.DoesNotExist:
            raise serializers.ValidationError('شهر پیدا نشد')
        return value

    def validate_address(self, value: 'str') -> 'str':
        return value.strip().lower()

    def validate_road_name(self, value: str) -> str:
        return value.strip().lower()

    def validate_postal_code(self, value):
        try:
            return str(int(value))
        except:
            raise serializers.ValidationError('لطفا کد پستی را صحیح وارد نمایید')
