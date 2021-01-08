from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class AdminDashboardView(UserPassesTestMixin, TemplateView):

    template_name = 'users/admin/dashboard.html'

    def test_func(self):
        return (self.request.user.is_authenticated and self.request.user.is_admin) or self.request.user.is_superuser
