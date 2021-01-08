from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class BuyerDashboardView(UserPassesTestMixin, TemplateView):

    template_name = 'users/buyer/dashboard.html'

    def test_func(self):
        return (self.request.user.is_authenticated and self.request.user.is_buyer) or self.request.user.is_superuser
