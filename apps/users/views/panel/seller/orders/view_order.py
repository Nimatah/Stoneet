from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import Order


class ViewOrderView(UserPassesTestMixin, DetailView):

    template_name = 'users/seller/orders/view_order.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'order'
    model = Order

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(product__user=self.request.user)

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_seller or self.request.user.is_superuser)
