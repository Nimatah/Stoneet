from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class SellerSampleListView(TemplateView):
    template_name = 'users/seller/orders/seller_sample_list.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_seller or self.request.user.is_superuser)
