from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from apps.home.models import StaticContent


class AdminConfigView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/configurations/config.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['static_content'] = StaticContent.objects.first()
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
