from django.views.generic import DetailView

from apps.users.models import User


class QCSellerDetailView(DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_seller.html'
    model = User
    pk_url_kwarg = 'pk'


class QCSellerListView(DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_list_sellers.html'
    model = User
    pk_url_kwarg = 'pk'


class QCLogisticDetailView(DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_logistic.html'
    model = User
    pk_url_kwarg = 'pk'


class QCLogisticListView(DetailView):
    template_name = 'users/admin/user_management/qc_user/qc_list_logistics.html'
    model = User
    pk_url_kwarg = 'pk'
