from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class QCProductView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/product_management/qc_product.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
