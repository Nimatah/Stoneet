from django.views.generic import TemplateView


class AdminOrdersView(TemplateView):
    template_name = 'users/admin/order_management/orders.html'
