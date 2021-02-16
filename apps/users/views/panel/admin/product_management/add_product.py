from django.views.generic import TemplateView


class AddProductView(TemplateView):
    template_name = 'users/admin/product_management/add_product.html'
