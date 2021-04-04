from django.views.generic import ListView

from apps.orders.models import Order
from apps.orders.filters import AdminOrderFilter


class AdminOrdersView(ListView):

    template_name = 'users/admin/order_management/orders.html'
    model = Order
    context_object_name = 'orders'
    paginate_by = 10
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = Order.objects.all()
        queryset = AdminOrderFilter(self.request.GET, queryset=queryset).qs
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['order_model'] = Order
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
