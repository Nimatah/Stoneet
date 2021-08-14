from django.views.generic import TemplateView


class EditAdminView(TemplateView):
    template_name = 'users/admin/user_management/edit_user/edit_admin.html'


class EditSellerView(TemplateView):
    template_name = 'users/admin/user_management/edit_user/edit_seller.html'


class EditBuyerView(TemplateView):
    template_name = 'users/admin/user_management/edit_user/edit_buyer.html'


class EditLogisticView(TemplateView):
    template_name = 'users/admin/user_management/edit_user/edit_logistic.html'
