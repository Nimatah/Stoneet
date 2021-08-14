from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class AddAdminView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/user_management/create_user/create_admin.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class AddSellerView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/user_management/create_user/create_seller.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class AddBuyerView(UserPassesTestMixin,TemplateView):
    template_name = 'users/admin/user_management/create_user/create_buyer.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class AddLogisticView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/user_management/create_user/create_logistic.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
