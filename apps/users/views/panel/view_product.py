from django.views.generic import DetailView

from apps.products.models import Product


class ViewProductView(DetailView):

    template_name = 'users/seller/view_product.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'product'
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
