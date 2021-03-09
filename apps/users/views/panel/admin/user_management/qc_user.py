from django.views.generic import TemplateView


class QCSellerView(TemplateView):
    template_name = 'users/admin/user_management/qc_user/qc_seller.html'


class QCSellerDetailsView(TemplateView):
    template_name = 'users/admin/user_management/qc_user/qc_list_sellers.html'


class QCLogisticView(TemplateView):
    template_name = 'users/admin/user_management/qc_user/qc_logistic.html'


class QCLogisticDetailsView(TemplateView):
    template_name = 'users/admin/user_management/qc_user/qc_list_logistics.html'
