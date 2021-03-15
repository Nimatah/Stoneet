from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    mobile_number = serializers.CharField()
    use_type = serializers.CharField(read_only=True)
    legal_type = serializers.CharField()
    state = serializers.CharField(source='get_state_display')
    full_name = serializers.CharField(source='profile.full_name', read_only=True)
    region = serializers.CharField(source='profile.region.title')

    class Meta:
        model = User
        fields = ('id', 'email', 'mobile_number', 'use_type', 'legal_type', 'state', 'full_name', 'region',)
        depth = 1
