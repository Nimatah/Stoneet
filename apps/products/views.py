from django.views.generic import TemplateView


class ProductDetailView(TemplateView):
    template_name = 'products/product_details.html'


class ListProductView(TemplateView):
    template_name = 'products/list_product.html'
