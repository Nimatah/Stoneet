from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.products.forms import CreateProductForm
from apps.products.models import Attribute, Category


class AddProductView(UserPassesTestMixin, FormView):
    form_class = CreateProductForm
    template_name = 'users/seller/products/add_product.html'
    success_url = reverse_lazy('users:seller_list_product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [c.to_dict_hierarchy() for c in Category.objects.get_root().prefetch_related('children')]
        context['attributes_field'] = Attribute.objects.get_by_input_field().filter(is_special=False).order_by('order')
        context['attributes_image'] = Attribute.objects.get_by_image_field().filter(is_special=False).order_by('order')
        context['attributes_bool'] = Attribute.objects.get_by_bool_field().filter(is_special=False).order_by('order')
        context['ID_SAMPLE'] = Attribute.ID_SAMPLE
        return context

    def form_valid(self, form):
        form.user = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_seller or self.request.user.is_superuser)
