from django.views.generic import DetailView

from apps.users.models import User


class QCSellerDetailView(DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_seller.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'seller'


class QCSellerListView(DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_list_sellers.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'sellers'


class QCBuyerDetailView(DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_buyer.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'buyer'


class QCBuyerListView(DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_list_buyers.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'buyers'


class QCLogisticDetailView(DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_logistic.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'logistic'


class QCLogisticListView(DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_list_logistics.html'
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'logistics'
