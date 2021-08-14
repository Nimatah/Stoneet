from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class AdminBuyerInvoiceView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/invoice_management/invoice_buyer.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class AdminSellerInvoiceView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/invoice_management/invoice_seller.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class AdminLogisticInvoiceView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/invoice_management/invoice_logistic.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
