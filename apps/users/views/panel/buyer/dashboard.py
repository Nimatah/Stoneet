from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import Order
from apps.invoices.models import Invoice


class BuyerDashboardView(UserPassesTestMixin, TemplateView):

    template_name = 'users/buyer/dashboard.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_buyer or self.request.user.is_superuser)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_queryset'] = Order.objects.get_by_buyer(self.request.user)

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_buyer or self.request.user.is_superuser)
