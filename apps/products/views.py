from django.views.generic import ListView, DetailView, TemplateView

from apps.products.models import Product, Attribute, Category
from apps.products.filters.products import UserProductFilter


class ListProductView(ListView):
    template_name = 'products/list_product.html'
    model = Product
    paginate_by = 12
    page_kwarg = 'p'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['nodes'] = Category.objects.get_root()
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(state=Product.STATE_ACCEPTED)
        queryset = UserProductFilter(self.request.GET, queryset=queryset, request=self.request).qs
        return queryset


class ProductDetailView(DetailView):
    template_name = 'products/product_details.html'
    model = Product
    pk_url_kwarg = 'pk'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['months'] = range(1, 13)
        context['payment_reverse_mapper'] = Attribute.PAYMENT_REVERSE_MAP
        return context


class BuyProductView(TemplateView):
    template_name = 'products/buy_product.html'
