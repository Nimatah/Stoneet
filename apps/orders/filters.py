from datetime import timedelta

import django_filters
from persiantools.jdatetime import JalaliDate

from apps.orders.models import Order, LogisticOrder


class OrderFilter(django_filters.FilterSet):

    date = django_filters.CharFilter(method='date_filter')
    id = django_filters.CharFilter(field_name='pk')
    product_id = django_filters.CharFilter(field_name='product', lookup_expr='pk')
    state = django_filters.CharFilter(field_name='state')

    def date_filter(self, queryset, name, value):
        date_filter = JalaliDate(*map(int, value.split('-'))).to_gregorian()
        date_range = date_filter + timedelta(days=1)
        return queryset.filter(timestamp__range=(date_filter, date_range))

    class Meta:
        model = Order
        fields = ['date', 'id', 'product_id', 'state', ]


class AdminOrderFilter(OrderFilter):

    buyer = django_filters.CharFilter(field_name='buyer', lookup_expr='pk')
    seller = django_filters.CharFilter(field_name='product__user', lookup_expr='pk')
    date = django_filters.CharFilter(method='date_filter')

    class Meta:
        model = Order
        fields = ['date', 'id', 'product_id', 'state', 'buyer', 'seller']

    def date_filter(self, queryset, name, value):
        date_filter = JalaliDate(*map(int, value.split('-'))).to_gregorian()
        date_range = date_filter + timedelta(days=1)
        return queryset.filter(timestamp__range=(date_filter, date_range))


class AdminLogisticOrderFilter(django_filters.FilterSet):

    date = django_filters.CharFilter(method='date_filter')
    id = django_filters.CharFilter(field_name="pk")
    order_id = django_filters.CharFilter(field_name='order__pk')
    state = django_filters.CharFilter(field_name='state')
    user = django_filters.CharFilter(field_name='user__profile__full_name', lookup_expr='icontains')

    def date_filter(self, queryset, name, value):
        date_filter = JalaliDate(*map(int, value.split('-'))).to_gregorian()
        date_range = date_filter + timedelta(days=1)
        return queryset.filter(timestamp__range=(date_filter, date_range))

    class Meta:
        model = LogisticOrder
        fields = ['date', 'id', 'order_id', 'state', 'user', ]
