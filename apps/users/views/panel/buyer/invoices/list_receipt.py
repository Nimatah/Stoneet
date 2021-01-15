from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.invoices.models import Receipt


class ListReceiptView(UserPassesTestMixin, ListView):

    template_name = 'users/buyer/invoices/list_receipt.html'
    paginate_by = 10
    context_object_name = 'receipts'
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = Receipt.objects.filter(product__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_buyer or self.request.user.is_superuser)
