from django.views.generic import DetailView, TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import LogisticOrder


class ViewLogisticOrderView(UserPassesTestMixin, TemplateView):

    template_name = 'users/logistic/logistic_orders/view_order.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'logistic_orders'
    model = LogisticOrder

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user=self.request.user)

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_logistic or self.request.user.is_superuser)
