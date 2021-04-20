from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from apps.orders.forms import AdminApproveOrderForm
from apps.orders.models import Order
from apps.products.models import Attribute


class AdminOrderQCView(FormMixin, DetailView):

    template_name = 'users/admin/order_management/order_qc.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'order'
    model = Order
    form_class = AdminApproveOrderForm

    def get_success_url(self):
        return reverse_lazy('users:admin_list_order')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment_map'] = Attribute.PAYMENT_MAP
        context['states'] = dict(Order.STATE_CHOICES)
        context['state_score_map'] = Order.STATE_ORDER_MAP
        context['contract'] = self.object.media.filter(title='contract').first()
        return context

    def form_valid(self, form):
        form.id = self.kwargs[self.pk_url_kwarg]
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
