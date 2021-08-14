from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import LogisticOrder
from apps.products.models import Attribute


class AdminLogisticOrderQCView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/order_management/logistic_order_qc.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'logistic_order'
    model = LogisticOrder

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment_map'] = Attribute.PAYMENT_MAP
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
