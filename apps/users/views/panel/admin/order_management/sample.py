from django.views.generic import TemplateView


class AdminSampleListView(TemplateView):
    template_name = 'users/admin/sample_management/samples.html'


class AdminSampleDetailView(TemplateView):
    template_name = 'users/admin/sample_management/sample_details.html'
