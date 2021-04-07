from django.views.generic import ListView

from apps.products.models import Product


class ListProductView(ListView):

    template_name = 'users/admin/product_management/list_product.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10
    page_kwarg = 'p'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
