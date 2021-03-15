from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import Order
from apps.products.models import Product
from apps.users.models import User, Mine


class AdminDashboardView(UserPassesTestMixin, TemplateView):

    template_name = 'users/admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_queryset'] = User.objects.all()
        context['products_queryset'] = Product.objects.all()
        context['orders_queryset'] = Order.objects.all()
        context['mines_queryset'] = Mine.objects.all()
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
