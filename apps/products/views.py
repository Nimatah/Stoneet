from django.views.generic import ListView, DetailView, TemplateView

from apps.products.models import Product


class ListProductView(ListView):
    template_name = 'products/list_product.html'
    model = Product
    paginate_by = 12
    page_kwarg = 'p'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'products/product_details.html'
    model = Product
    pk_url_kwarg = 'pk'
    context_object_name = 'product'


class BuyProductView(TemplateView):
    template_name = 'products/buy_product.html'
