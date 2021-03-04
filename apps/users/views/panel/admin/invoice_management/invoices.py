from django.views.generic import TemplateView


class AdminBuyerInvoiceView(TemplateView):
    template_name = 'users/admin/invoice_management/invoice_buyer.html'


class AdminSellerInvoiceView(TemplateView):
    template_name = 'users/admin/invoice_management/invoice_seller.html'


class AdminLogisticInvoiceView(TemplateView):
    template_name = 'users/admin/invoice_management/invoice_logistic.html'
