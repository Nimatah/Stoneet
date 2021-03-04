from django.views.generic import TemplateView


class AdminBuyerInvoiceDetailsView(TemplateView):
    template_name = 'users/admin/invoice_management/invoice_details_buyer.html'


class AdminSellerInvoiceDetailsView(TemplateView):
    template_name = 'users/admin/invoice_management/invoice_details_seller.html'


class AdminLogisticInvoiceDetailsView(TemplateView):
    template_name = 'users/admin/invoice_management/invoice_details_logistic.html'

