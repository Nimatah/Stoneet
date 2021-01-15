from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import LogisticOrder


class ListLogisticOrderView(UserPassesTestMixin, ListView):

    template_name = 'users/logistic/logistic_orders/list_order.html'
    paginate_by = 10
    context_object_name = 'logistic_orders'
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = LogisticOrder.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_logistic or self.request.user.is_superuser)
