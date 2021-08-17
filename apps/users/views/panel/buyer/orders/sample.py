from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import SampleOrder


class BuyerSampleListView(UserPassesTestMixin, ListView):

    template_name = 'users/buyer/orders/buyer_sample_list.html'
    model = SampleOrder
    context_object_name = 'samples'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_buyer or self.request.user.is_superuser)
