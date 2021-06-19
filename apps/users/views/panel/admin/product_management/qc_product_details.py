from django.views.generic import DetailView

from apps.products.models import Product


class QCProductDetailsView(DetailView):
    template_name = 'users/admin/product_management/qc_product_details.html'
    model = Product
    pk_url_kwarg = 'pk'
    context_object_name = 'product'
