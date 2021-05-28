from django.views.generic import TemplateView

from apps.home.models import StaticContent


class AdminConfigView(TemplateView):
    template_name = 'users/admin/configurations/config.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['static_content'] = StaticContent.objects.first()
        return context
