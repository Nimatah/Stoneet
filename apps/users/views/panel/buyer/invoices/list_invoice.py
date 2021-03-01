from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.invoices.models import Invoice


class ListInvoiceView(UserPassesTestMixin, TemplateView):

    template_name = 'users/buyer/invoices/list_invoice.html'
    paginate_by = 10
    context_object_name = 'invoices'
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = Invoice.objects.filter(product__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_buyer or self.request.user.is_superuser)
