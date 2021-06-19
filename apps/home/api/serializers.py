from rest_framework import serializers

from ..models import StaticContent


class StaticContentSerializer(serializers.ModelSerializer):
    terms = serializers.CharField()
    terms_seller = serializers.CharField()
    terms_logistic = serializers.CharField()
    privacy_policy = serializers.CharField()
    about_us = serializers.CharField()

    class Meta:
        model = StaticContent
        fields = ('terms', 'terms_seller', 'terms_logistic', 'privacy_policy', 'about_us',)
