from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.products.models import Product
from apps.orders.models import Order


class SellerDashboardView(UserPassesTestMixin, TemplateView):

    template_name = 'users/seller/dashboard.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_seller or self.request.user.is_superuser)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_queryset'] = Product.objects.get_by_user(self.request.user)
        context['order_queryset'] = Order.objects.get_by_seller(self.request.user)
        return context
