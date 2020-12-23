from django.views.generic import ListView

from apps.products.models import Product


class ListProductView(ListView):

    template_name = 'users/seller/list_product.html'
    paginate_by = 50
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
