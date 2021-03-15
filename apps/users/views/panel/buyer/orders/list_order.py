from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.products.models import Attribute
from apps.orders.models import Order


class ListOrderView(UserPassesTestMixin, ListView):

    template_name = 'users/buyer/orders/list_order.html'
    paginate_by = 10
    context_object_name = 'orders'
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = Order.objects.filter(buyer=self.request.user)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['payment_map'] = Attribute.PAYMENT_MAP
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_buyer or self.request.user.is_superuser)
