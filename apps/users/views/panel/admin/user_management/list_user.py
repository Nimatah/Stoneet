from django.views.generic import TemplateView


class ListAdminView(TemplateView):
    template_name = 'users/admin/user_management/list_user/list_admin.html'


class ListSellerView(TemplateView):
    template_name = 'users/admin/user_management/list_user/list_seller.html'


class ListBuyerView(TemplateView):
    template_name = 'users/admin/user_management/list_user/list_buyer.html'


class ListLogisticView(TemplateView):
    template_name = 'users/admin/user_management/list_user/list_logistic.html'


