from django.views.generic import TemplateView


class ListProductView(TemplateView):
    template_name = 'users/admin/product_management/list_product.html'
