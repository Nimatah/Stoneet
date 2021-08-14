from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.products.models import Product


class QCProductDetailsView(DetailView):
    template_name = 'users/admin/product_management/qc_product_details.html'
    model = Product
    pk_url_kwarg = 'pk'
    context_object_name = 'product'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
