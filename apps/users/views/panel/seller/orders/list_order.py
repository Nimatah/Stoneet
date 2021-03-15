from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import Order
from apps.products.models import Attribute


class ListOrderView(UserPassesTestMixin, ListView):

    template_name = 'users/seller/orders/list_order.html'
    paginate_by = 10
    context_object_name = 'orders'
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = Order.objects.filter(product__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment_map'] = Attribute.PAYMENT_MAP
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_seller or self.request.user.is_superuser)
