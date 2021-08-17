from django.views.generic import FormView
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

from apps.products.models import Product
from .models import SampleOrder
from .forms import CreateOrderForm


class OrderFormView(UserPassesTestMixin, FormView):

    form_class = CreateOrderForm
    template_name = 'products/buy_product.html'

    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound()

    def form_valid(self, form):
        form.buyer = self.request.user
        order = form.save()
        self.pk = order.pk
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('users:buyer_view_order', kwargs={'pk': self.pk})

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_buyer or self.request.user.is_superuser)


def create_sample_order(request):
    if not request.user.is_authenticated and not (request.user.is_buyer or request.user.is_superuser):
        return HttpResponseForbidden()

    product_id = request.POST.get('product_id')
    if not product_id:
        return HttpResponseNotFound()

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponseNotFound()

    SampleOrder.objects.create(product=product, buyer=request.user, state=SampleOrder.STATE_PENDING)

    return redirect(reverse_lazy('users:buyer_sample_list'))
