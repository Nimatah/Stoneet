from django.views.generic import TemplateView


class AdminOrderQCView(TemplateView):
    template_name = 'users/admin/order_management/order_qc.html'
