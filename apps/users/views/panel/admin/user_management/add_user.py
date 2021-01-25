from django.views.generic import TemplateView


class AddAdminView(TemplateView):
    template_name = 'users/admin/user_management/create_user/create_admin.html'


class AddSellerView(TemplateView):
    template_name = 'users/admin/user_management/create_user/create_seller.html'


class AddBuyerView(TemplateView):
    template_name = 'users/admin/user_management/create_user/create_buyer.html'


class AddLogisticView(TemplateView):
    template_name = 'users/admin/user_management/create_user/create_logistic.html'
