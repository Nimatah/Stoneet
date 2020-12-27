from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.products.models import Product, Category
from apps.products.filters import ProductFilter


class ListProductView(UserPassesTestMixin, ListView):

    template_name = 'users/seller/list_product.html'
    paginate_by = 10
    context_object_name = 'products'
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = Product.objects.filter(user=self.request.user).prefetch_related('attributes', 'media')
        queryset = ProductFilter(self.request.GET, queryset=queryset).qs
        return queryset

    def test_func(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [c.to_dict_hierarchy() for c in Category.objects.get_root().prefetch_related('children')]
        return context
