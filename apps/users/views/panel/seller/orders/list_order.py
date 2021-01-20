from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import Order


class ListOrderView(UserPassesTestMixin, ListView):

    template_name = 'users/seller/orders/list_order.html'
    paginate_by = 10
    context_object_name = 'orders'
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = Order.objects.filter(product__user=self.request.user)
        # queryset = ProductFilter(self.request.GET, queryset=queryset).qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = [c.to_dict_hierarchy() for c in Category.objects.get_root().prefetch_related('children')]
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_seller or self.request.user.is_superuser)
