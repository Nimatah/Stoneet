from django.views.generic import TemplateView


class AdminSampleListView(TemplateView):
    template_name = 'users/admin/order_management/admin_sample_list.html'


class AdminSampleDetailView(TemplateView):
    template_name = 'users/admin/order_management/admin_sample_detail.html'
