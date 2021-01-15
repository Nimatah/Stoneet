from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.products.models import Product


class ViewProductView(UserPassesTestMixin, DetailView):

    template_name = 'users/seller/view_product.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'product'
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_seller or self.request.user.is_superuser)
