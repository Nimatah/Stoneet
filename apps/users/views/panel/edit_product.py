from django.views.generic import UpdateView
from django.urls import reverse_lazy

from apps.products.forms import EditProductForm
from apps.products.models import Product


class EditProductView(UpdateView):

    template_name = 'users/seller/edit_product.html'
    form_class = EditProductForm
    pk_url_kwarg = 'pk'
    context_object_name = 'product'
    model = Product
    success_url = reverse_lazy('users:list_product')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user).prefetch_related('attributes', 'media')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
