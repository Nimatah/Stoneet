from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from apps.users.models import User, Profile


class AddAdminView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/user_management/create_user/create_admin.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class AddSellerView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/user_management/create_user/create_seller.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = User.objects.create(
                use_type=data['use_type'],
                username=data['email'],
                mobile_number=data['mobile_number'],
                email=data['email'],
                legal_type=data['legal_type']
            )
        
        if data['legal_type'] == User.LEGAL_INDIVIDUAL:
            profile = Profile()
            profile.first_name = data['first_name']
            profile.last_name = data['last_name']
            profile.birthday = data['birthday']
            profile.gender = data['gender']
            profile.id_code = data['id_code']
            profile.national_code = data['national_code']
            profile.address = data['address']
            profile.postal_code = data['postal_code']
            profile.region_id = data['region']
            profile.phone_number = data['phone_number']
            profile.bank_account_name = data['bank_account_name']
            profile.bank_account_number = data['bank_account_number']
            profile.bank_sheba_number = data['bank_sheba_number']
        elif data['legal_type'] == User.LEGAL_LEGAL:
            profile = Profile()
            profile.address = data['address']
            profile.postal_code = data['postal_code']
            profile.region_id = data['region']
            profile.phone_number = data['phone_number']
            profile.bank_account_name = data['bank_account_name']
            profile.bank_account_number = data['bank_account_number']
            profile.bank_sheba_number = data['bank_sheba_number']
            profile.company_name = data['company_name']
            profile.company_type = data['company_type']
            profile.company_register_code = data['company_register_code']
            profile.company_national_code = data['company_national_code']
            profile.company_finance_code = data['company_finance_code']
            profile.company_print_signature_right = data['company_print_signature_right']
            
        user.save()
        user.profile = profile
        user.profile.save()
        
        return redirect(reverse_lazy('users:admin_list_seller'))


class AddBuyerView(UserPassesTestMixin,TemplateView):
    template_name = 'users/admin/user_management/create_user/create_buyer.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class AddLogisticView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/user_management/create_user/create_logistic.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
