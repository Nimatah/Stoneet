from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.products.models import Attribute, Category
from apps.users.models import User


class AddProductView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/product_management/add_product.html'

    def get(self, request, *args, **kwargs):
        if not self.request.GET.get('seller'):
            return HttpResponseBadRequest()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [c.to_dict_hierarchy() for c in Category.objects.get_root().prefetch_related('children')]
        context['attributes_field'] = Attribute.objects.get_by_input_field().filter(is_special=False).order_by('order')
        context['attributes_image'] = Attribute.objects.get_by_image_field().filter(is_special=False).order_by('order')
        context['attributes_bool'] = Attribute.objects.get_by_bool_field().filter(is_special=False).order_by('order')
        context['ID_SAMPLE'] = Attribute.ID_SAMPLE
        context['seller'] = User.objects.get(pk=self.request.GET.get('seller'))
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
