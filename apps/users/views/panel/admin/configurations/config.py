from django.views.generic import TemplateView


class AdminConfigView(TemplateView):
    template_name = 'users/admin/configurations/config.html'
