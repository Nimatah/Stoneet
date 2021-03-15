from rest_framework import serializers

from ..models import StaticContent


class StaticContentSerializer(serializers.ModelSerializer):
    terms = serializers.CharField()
    terms_conditions = serializers.CharField()
    terms_logistic = serializers.CharField()
    privacy_policy = serializers.CharField()

    class Meta:
        model = StaticContent
        fields = ('terms', 'terms_conditions', 'terms_logistic', 'privacy_policy',)
