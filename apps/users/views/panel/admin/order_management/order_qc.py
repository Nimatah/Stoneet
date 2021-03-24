from django.views.generic import DetailView

from apps.orders.models import Order
from apps.products.models import Attribute


class AdminOrderQCView(DetailView):
    template_name = 'users/admin/order_management/order_qc.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'order'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment_map'] = Attribute.PAYMENT_MAP
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
