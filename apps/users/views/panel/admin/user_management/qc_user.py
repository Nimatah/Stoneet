from django.views.generic import TemplateView


class QCSellerView(TemplateView):
    template_name = 'users/admin/user_management/qc_user/qc_seller.html'


class QCLogisticView(TemplateView):
    template_name = 'users/admin/user_management/qc_user/qc_logistic.html'
