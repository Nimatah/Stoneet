from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.invoices.models import Invoice
from apps.orders.models import Order


class ViewOrderView(UserPassesTestMixin, DetailView):

    template_name = 'users/buyer/orders/view_order.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'order'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seller_invoice'] = self.object.invoice_set.filter(type=Invoice.TYPE_SELLER).first()
        context['logistic_invoice'] = self.object.invoice_set.filter(type=Invoice.TYPE_LOGISTIC).first()
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_buyer or self.request.user.is_superuser)
