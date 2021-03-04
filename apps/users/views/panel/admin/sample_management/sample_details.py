from django.views.generic import TemplateView


class AdminSampleDetailsView(TemplateView):
    template_name = 'users/admin/sample_management/sample_details.html'
