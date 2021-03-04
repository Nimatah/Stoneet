from django.views.generic import TemplateView


class AdminSampleView(TemplateView):
    template_name = 'users/admin/sample_management/samples.html'
