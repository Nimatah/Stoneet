import django_filters

from apps.users.models import User


class AdminUserFilter(django_filters.FilterSet):

    id = django_filters.CharFilter(field_name='pk')
    name = django_filters.CharFilter(field_name='profile__full_name', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontians')
    city = django_filters.CharFilter(field_name='profile__region__title', lookup_expr='icontains')
    national_code = django_filters.CharFilter(field_name='profile__national_code', lookup_expr='icontains')
    financial_code = django_filters.CharFilter(field_name='profile__financial_code', lookup_expr='icontains')
    mobile_number = django_filters.CharFilter(field_name='mobile_number', lookup_expr='icontains')
    state = django_filters.CharFilter(field_name='state')

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'city', 'national_code', 'financial_code', 'mobile_number', 'state']
