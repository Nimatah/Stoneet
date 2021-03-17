from django.views.generic import ListView

from apps.orders.models import Order


class AdminOrdersView(ListView):

    template_name = 'users/admin/order_management/orders.html'
    model = Order
    context_object_name = 'orders'
