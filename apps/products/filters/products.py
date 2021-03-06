import django_filters

from apps.products.models import Product, Category


class ProductFilter(django_filters.FilterSet):

    category = django_filters.CharFilter(method='category_filter')
    scategory = django_filters.CharFilter(field_name='category', lookup_expr='pk')
    state = django_filters.CharFilter(field_name='state')
    q = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    def category_filter(self, queryset, name, value):
        category = Category.objects.get(pk=value)
        category_list = category.get_descendants(include_self=True)
        return queryset.filter(category_id__in=category_list)

    class Meta:
        model = Product
        fields = ['category', 'scategory', 'state', 'q', ]


class AdminProductFilter(django_filters.FilterSet):

    id = django_filters.CharFilter(field_name='pk')
    seller_id = django_filters.CharFilter(field_name='user', lookup_expr='pk')
    category = django_filters.CharFilter(method='category_filter')
    state = django_filters.CharFilter(field_name='state')
    q = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    def category_filter(self, queryset, name, value):
        category = Category.objects.get(pk=value)
        category_list = category.get_descendants(include_self=True)
        return queryset.filter(category_id__in=category_list)

    class Meta:
        model = Product
        fields = ['id', 'category', 'state', 'q']


class UserProductFilter(django_filters.FilterSet):

    q = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    category = django_filters.CharFilter(method='category_filter')

    def category_filter(self, queryset, name, value):
        return queryset.filter(category_id__in=self.request.GET.getlist('category'))

    class Meta:
        model = Product
        fields = ['category', 'q', ]
