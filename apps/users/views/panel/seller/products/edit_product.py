from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import transaction
from persiantools.digits import ar_to_fa, fa_to_en

from apps.products.models import Product, Attribute, Category, AttributeMedia, ProductMedia, ProductAttribute


class EditProductView(UserPassesTestMixin, DetailView):

    template_name = 'users/seller/products/edit_product.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'product'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Attribute'] = Attribute
        context['categories'] = [c.to_dict_hierarchy() for c in Category.objects.get_root().prefetch_related('children')]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user).prefetch_related('attributes', 'media')

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_seller or self.request.user.is_superuser)

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES

        product = Product.objects.get(pk=kwargs['pk'])
        product.category_id = data.get('category')
        product.mine_id = data.get('mine')
        with transaction.atomic():
            product.attributes.all().delete()
            attributes = {''.join(filter(str.isdigit, k)): {} for k in data.keys() if k.startswith('attribute') and k != 'attribute_9'}
            for k, v in data.items():
                if k.startswith('attribute_'):
                    key = k.replace('attribute_', '')
                    if key == '9':
                        continue
                    if key.isdigit():
                        attributes[key]['value'] = data.get(k)
                    if '_to' in key:
                        key = key.replace('_to', '')
                        attributes[key]['value'] = data.get(k)
                    if '_from' in key:
                        key = key.replace('_from', '')
                        attributes[key]['value'] = data.get(k)
                    if 'child_' in key:
                        key = key.replace('child_', '')
                        attributes[key]['child_value'] = data.get(k)
                    if 'weight_' in key:
                        key = key.replace('weight_', '')
                        attributes[key]['weight'] = data.get(k)

            analyze = product.get_analyze()
            if analyze:
                analyze.file = files.get('analyze')
                analyze.save()
            else:
                product_attribute = product.attributes.create(attribute_id=Attribute.ID_ANALYZE)
                AttributeMedia.objects.create(
                    product_attribute=product_attribute,
                    type=AttributeMedia.TYPE_IMAGE,
                    file=data.get('analyze'),
                )

            try:
                primary_image = product.media.get(is_primary=True)
                primary_image.file = files.get('primary_image')
                primary_image.save()
            except ProductMedia.DoesNotExist:
                product.media.create(
                    type=ProductMedia.TYPE_IMAGE,
                    file=files.get('primary_image')
                )

            for k, v in attributes.items():
                if v['value'] == 'on':
                    v['value'] = True
                elif v['value'] == 'off':
                    v['value'] = False
                if isinstance(v['value'], str):
                    fa_to_en(ar_to_fa(v['value'].strip()))
                    fa_to_en(ar_to_fa(v['value'].strip()))

                attr = ProductAttribute()
                attr.attribute_id = int(k)
                attr.product = product
                attr.value = v['value']
                if attr.attribute.has_child_value:
                    attr.child_value = fa_to_en(ar_to_fa(v['child_value'].strip()))
                if 'weight' in v:
                    attr.weight_unit = v['weight']
                attr.save()

            payment_type = data.getlist('attribute_9')

            additional_images = product.media.filter(is_primary=False)
            additional_files = filter(str.startswith, files.keys())
            for i, v in enumerate(additional_files):
                additional_images[i].file = v
                additional_images[i].save()

        return redirect(reverse_lazy('users:seller_edit_product', kwargs={'pk': kwargs['pk']}))
