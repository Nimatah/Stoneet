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
        product.description = data.get('description')
        with transaction.atomic():
            product.attributes.all().exclude(attribute_id=Attribute.ID_ANALYZE).delete()
            attributes = {''.join(filter(str.isdigit, k)): {} for k in data.keys() if k.startswith('attribute') and k != 'attribute_9[]'}
            for k, v in data.items():
                if k.startswith('attribute_'):
                    key = k.replace('attribute_', '')
                    if key == '9[]':
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
                if files.get('analyze'):
                    analyze.media.all().first().file = files.get('analyze')
                    analyze.save()
            else:
                product_attribute = ProductAttribute.objects.create(attribute_id=Attribute.ID_ANALYZE, product=product)
                AttributeMedia.objects.create(
                    product_attribute=product_attribute,
                    type=AttributeMedia.TYPE_IMAGE,
                    file=files.get('analyze'),
                )

            try:
                if files.get('image_primary'):
                    primary_image = product.media.get(is_primary=True)
                    primary_image.file = files.get('image_primary')
                    primary_image.save()
            except ProductMedia.DoesNotExist:
                product.media.create(
                    type=ProductMedia.TYPE_IMAGE,
                    file=files.get('image_primary'),
                    is_primary=True
                )
            attributes.pop('5')
            for k, v in attributes.items():
                if 'value' not in v:
                    continue
                if v['value'] == 'on':
                    v['value'] = True
                elif v['value'] == 'off':
                    v['value'] = False
                if isinstance(v['value'], str):
                    v['value'] = fa_to_en(ar_to_fa(v['value'].strip()))
                    v['value'] = fa_to_en(ar_to_fa(v['value'].strip()))

                attr = ProductAttribute()
                attr.attribute_id = int(k)
                attr.product = product
                attr.value = v['value']
                if attr.attribute.has_child_value:
                    attr.child_value = fa_to_en(ar_to_fa(v['child_value'].strip()))
                if 'weight' in v:
                    attr.weight_unit = v['weight']
                attr.save()

            payment_type = data.getlist('attribute_9[]')
            attr = ProductAttribute()
            attr.attribute_id = 9
            attr.value = '|'.join(payment_type)
            attr.product = product
            attr.save()

            sample = data.get('attribute_child_5')
            if sample and data.get('attribute_5'):
                attr = ProductAttribute()
                attr.attribute_id = 5
                attr.value = int(sample)
                attr.product = product
                attr.save()

            additional_images = product.media.filter(is_primary=False)
            additional_files = list(filter(lambda x: x.replace('image_', '').isdigit() and x != 'image_primary', list(files.keys())))
            for i, v in enumerate(additional_files):
                try:
                    additional_images[i].file = files.get(v)
                    additional_images[i].save()
                except IndexError:
                    ProductMedia.objects.create(
                        product=product,
                        type=ProductMedia.TYPE_IMAGE,
                        file=files.get(v),
                        is_primary=False,
                    )
            ayar = 'عیار'
            if product.get_min_caret().value == product.get_max_caret().value:
                product.title = f'{product.category.title} {ayar} {product.get_min_caret().value} %'
            else:
                product.title = f'{product.category.title} {ayar} {product.get_max_caret().value} - {product.get_min_caret().value} %'
            product.save()

        return redirect(reverse_lazy('users:seller_edit_product', kwargs={'pk': kwargs['pk']}))
