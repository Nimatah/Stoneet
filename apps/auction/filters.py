import django_filters

from apps.auction.models import Auction


class AdminAuctionFilter(django_filters.FilterSet):

    id = django_filters.CharFilter(field_name='pk')
    user = django_filters.CharFilter(field_name='winner__profile__full_name', lookup_expr='icontains')
    order = django_filters.CharFilter(field_name='order__pk')
    source = django_filters.CharFilter(field_name='order__product__mine__region__parent__title', lookup_expr='icontains')
    destination = django_filters.CharFilter(field_name='order__destination__region__parent__title', lookup_expr='icontains')

    class Meta:
        model = Auction
        fields = ['id', 'user', 'order', 'source', 'destination']
