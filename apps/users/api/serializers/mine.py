from rest_framework import serializers

from apps.users.models import Mine
from apps.locations.models import Region


class MineSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    region_id = serializers.IntegerField()
    address = serializers.CharField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    road_name = serializers.CharField()
    location_in_region = serializers.CharField()
    distance_to_road = serializers.IntegerField()
    proper_road = serializers.BooleanField()
    load_tools = serializers.BooleanField()

    class Meta:
        model = Mine
        fields = ('title', 'region_id', 'user', 'address', 'road_name', 'location_in_region',
                  'distance_to_road', 'proper_road', 'load_tools',)

    def validate_title(self, value: str) -> str:
        return value.strip().lower()

    def validate_region_id(self, value: int) -> int:
        try:
            Region.objects.get(pk=value)
        except Region.DoesNotExist:
            raise serializers.ValidationError('region not found')
        return value

    def validate_address(self, value: 'str') -> 'str':
        return value.strip().lower()

    def validate_road_name(self, value: str) -> str:
        return value.strip().lower()
