from django.views.generic import ListView

from apps.products.models import Product, Category
from apps.products.filters import AdminProductFilter


class ListProductView(ListView):

    template_name = 'users/admin/product_management/list_product.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = AdminProductFilter(self.request.GET, queryset=queryset).qs
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['product_states'] = dict(Product._STATE_CHOICES)
        context['categories'] = Category.objects.get_leaf()
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
