from django.views.generic import TemplateView


class ProductDetailView(TemplateView):
    template_name = 'products/product_details.html'
