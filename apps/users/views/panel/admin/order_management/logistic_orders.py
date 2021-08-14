from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.filters import AdminLogisticOrderFilter
from apps.orders.models import LogisticOrder


class AdminLogisticOrdersView(UserPassesTestMixin, ListView):

    template_name = 'users/admin/order_management/logistic_orders.html'
    model = LogisticOrder
    context_object_name = 'logistic_orders'
    paginate_by = 10
    page_kwarg = 'p'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['logistic_order_model'] = LogisticOrder
        return context

    def get_queryset(self):
        queryset = LogisticOrder.objects.all()
        queryset = AdminLogisticOrderFilter(self.request.GET, queryset=queryset).qs
        return queryset

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
