from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.orders.models import SampleOrder


class AdminSampleDetailsView(UserPassesTestMixin, DetailView):
    template_name = 'users/admin/sample_management/sample_details.html'
    model = SampleOrder
    pk_url_kwarg = 'pk'
    context_object_name = 'sample'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
