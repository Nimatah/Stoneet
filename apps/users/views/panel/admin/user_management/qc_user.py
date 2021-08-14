from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.users.models import User


class QCSellerDetailView(UserPassesTestMixin, DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_seller.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'seller'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class QCSellerListView(UserPassesTestMixin, DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_list_sellers.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'sellers'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class QCBuyerDetailView(UserPassesTestMixin, DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_buyer.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'buyer'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class QCBuyerListView(UserPassesTestMixin, DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_list_buyers.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'buyers'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class QCLogisticDetailView(UserPassesTestMixin, DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_logistic.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'logistic'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class QCLogisticListView(UserPassesTestMixin, DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_list_logistics.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'logistics'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
