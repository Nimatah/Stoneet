from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class UserDashboardView(UserPassesTestMixin, TemplateView):

    template_name = 'users/seller/dashboard.html'

    def test_func(self):
        return self.request.user.is_authenticated
