from rest_framework import serializers

from apps.users.models import User, Mine
from apps.locations.models import Region


class MineSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    region_id = serializers.IntegerField()
    address = serializers.CharField()
    user_id = serializers.IntegerField()
    road_name = serializers.CharField()
    distance_to_road = serializers.IntegerField()
    proper_road = serializers.BooleanField()
    load_tools = serializers.BooleanField()

    class Meta:
        model = Mine
        fields = ('title', 'region_id', 'address', 'user_id', 'road_name',
                  'distance_to_road', 'proper_road', 'load_tools',)

    def validate_title(self, value: str) -> str:
        return value.strip().lower()

    def validate_region_id(self, value: int) -> 'Region':
        try:
            return Region.objects.get(pk=value)
        except Region.DoesNotExist:
            raise serializers.ValidationError('region not found')

    def validate_address(self, value: 'str') -> 'str':
        return value.strip().lower()

    def validate_user_id(self, value: int) -> 'User':
        try:
            return User.objects.get(pk=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('user not found')

    def validate_road_name(self, value: str) -> str:
        return value.strip().lower()

    def validate_distance_to_road(self, value: str) -> str:
        return value.strip().lower()
