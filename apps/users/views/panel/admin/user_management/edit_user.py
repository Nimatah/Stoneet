from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from persiantools.jdatetime import JalaliDate

from apps.users.models import User, Profile
from apps.locations.models import Region


class EditAdminView(DetailView):
    template_name = 'users/admin/user_management/edit_user/edit_admin.html'
    model = User
    context_object_name = 'admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        with transaction.atomic():
            user = User.objects.get(pk=kwargs['pk'])

            user.email = data['email']
            user.mobile_number = data['mobile_number']

            user.profile.first_name = data['first_name']
            user.profile.last_name = data['last_name']
            user.profile.birthday = JalaliDate(*map(lambda x: int(x), data['birthday'].split('-'))).to_gregorian()
            user.profile.gender = data['gender']
            user.profile.id_code = data['id_code']
            user.profile.national_code = data['national_code']
            user.profile.address = data['address']
            user.profile.postal_code = data['postal_code']
            user.profile.region_id = data['region']
            user.profile.phone_number = data['phone_number']

            user.save()
            user.profile.save()
        return redirect(reverse_lazy('users:admin_list_admin'))


class EditSellerView(DetailView):
    template_name = 'users/admin/user_management/edit_user/edit_seller.html'
    model = User
    context_object_name = 'seller'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context


class EditBuyerView(DetailView):
    template_name = 'users/admin/user_management/edit_user/edit_buyer.html'
    model = User
    context_object_name = 'buyer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context


class EditLogisticView(DetailView):
    template_name = 'users/admin/user_management/edit_user/edit_logistic.html'
    model = User
    context_object_name = 'logistic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context
