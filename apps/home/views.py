from django.views.generic import TemplateView

from apps.products.models import Product


class HomeView(TemplateView):

    PRODUCTS_LIMIT = 8

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter()[:self.PRODUCTS_LIMIT]
        return context
