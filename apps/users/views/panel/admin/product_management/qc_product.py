from django.views.generic import TemplateView


class QCProductView(TemplateView):
    template_name = 'users/admin/product_management/qc_product.html'
