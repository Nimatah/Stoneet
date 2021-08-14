from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class AdminSampleView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/sample_management/samples.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
