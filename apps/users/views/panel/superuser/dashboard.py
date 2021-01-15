from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class SuperuserDashboardView(UserPassesTestMixin, TemplateView):

    template_name = 'users/superuser/dashboard.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
