from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class AdminBuyerInvoiceDetailsView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/invoice_management/invoice_details_buyer.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class AdminSellerInvoiceDetailsView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/invoice_management/invoice_details_seller.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class AdminLogisticInvoiceDetailsView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/invoice_management/invoice_details_logistic.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)

