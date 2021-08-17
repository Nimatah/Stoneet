from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import SampleOrder


class SellerSampleListView(UserPassesTestMixin, ListView):
    template_name = 'users/seller/orders/seller_sample_list.html'
    model = SampleOrder
    context_object_name = 'samples'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_seller or self.request.user.is_superuser)
