from django.views.generic import TemplateView


class QCProductDetailsView(TemplateView):
    template_name = 'users/admin/product_management/qc_product_details.html'
