from django.db import transaction
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from persiantools.jdatetime import JalaliDate

from apps.users.models import User, Profile, UserMedia
from apps.locations.models import Region


class AddAdminView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/user_management/create_user/create_admin.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        with transaction.atomic():
            user = User.objects.create(
                use_type=User.TYPE_ADMIN,
                username=data['email'],
                mobile_number=data['mobile_number'],
                email=data['email'],
                legal_type=data['legal_type']
            )

            profile = Profile()
            profile.first_name = data['first_name']
            profile.last_name = data['last_name']
            profile.birthday = JalaliDate(*map(lambda x: int(x), data['birthday'].split('-'))).to_gregorian()
            profile.gender = data['gender']
            profile.id_code = data['id_code']
            profile.national_code = data['national_code']
            profile.address = data['address']
            profile.postal_code = data['postal_code']
            profile.region_id = data['region']
            profile.phone_number = data['phone_number']

            user.save()
            user.profile = profile
            user.profile.save()

        return redirect(reverse_lazy('users:admin_list_admin'))


class AddSellerView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/user_management/create_user/create_seller.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES

        if data.get('legal_type') == User.LEGAL_INDIVIDUAL:
            with transaction.atomic():
                user = User.objects.create(
                    use_type=User.TYPE_BUYER,
                    username=data['email'],
                    mobile_number=data['mobile_number'],
                    email=data['email'],
                    legal_type=data['legal_type']
                )

                profile = Profile()
                profile.first_name = data['first_name']
                profile.last_name = data['last_name']
                profile.birthday = JalaliDate(*map(lambda x: int(x), data['birthday'].split('-'))).to_gregorian()
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

                user.save()
                user.profile = profile
                user.profile.save()

                user.media.create(
                    title=UserMedia.name_map['image_id_card_front'],
                    file=files['image_id_card_front'],
                    type=UserMedia
                )
                user.media.create(
                    title=UserMedia.name_map['image_id_card_back'],
                    file=files['image_id_card_back'],
                    type=UserMedia
                )

        else:
            with transaction.atomic():
                user = User.objects.create(
                    use_type=User.TYPE_SELLER,
                    username=data['email'],
                    mobile_number=data['mobile_number'],
                    email=data['email'],
                    legal_type=data['legal_type']
                )

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

                user.media.create(
                    title=UserMedia.name_map['image_company_registration'],
                    file=files['image_company_registration'],
                    type=UserMedia
                )
                user.media.create(
                    title=UserMedia.name_map['image_company_latest_newspaper'],
                    file=files['image_company_latest_newspaper'],
                    type=UserMedia
                )
                user.media.create(
                    title=UserMedia.name_map['image_company_tax_on_added_value_certificate'],
                    file=files['image_company_tax_on_added_value_certificate'],
                    type=UserMedia
                )

        return redirect(reverse_lazy('users:admin_list_seller'))


class AddBuyerView(UserPassesTestMixin,TemplateView):
    template_name = 'users/admin/user_management/create_user/create_buyer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES

        if data.get('legal_type') == User.LEGAL_INDIVIDUAL:
            with transaction.atomic():
                user = User.objects.create(
                    use_type=User.TYPE_BUYER,
                    username=data['email'],
                    mobile_number=data['mobile_number'],
                    email=data['email'],
                    legal_type=data['legal_type']
                )
    
                profile = Profile()
                profile.first_name = data['first_name']
                profile.last_name = data['last_name']
                profile.birthday = JalaliDate(*map(lambda x: int(x), data['birthday'].split('-'))).to_gregorian()
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
    
                user.save()
                user.profile = profile
                user.profile.save()

                user.media.create(
                    title=UserMedia.name_map['image_id_card_front'],
                    file=files['image_id_card_front'],
                    type=UserMedia
                )
                user.media.create(
                    title=UserMedia.name_map['image_id_card_back'],
                    file=files['image_id_card_back'],
                    type=UserMedia
                )
        else:
            with transaction.atomic():
                user = User.objects.create(
                    use_type=User.TYPE_BUYER,
                    username=data['email'],
                    mobile_number=data['mobile_number'],
                    email=data['email'],
                    legal_type=data['legal_type']
                )

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

                user.media.create(
                    title=UserMedia.name_map['image_company_registration'],
                    file=files['image_company_registration'],
                    type=UserMedia
                )
                user.media.create(
                    title=UserMedia.name_map['image_company_latest_newspaper'],
                    file=files['image_company_latest_newspaper'],
                    type=UserMedia
                )
                user.media.create(
                    title=UserMedia.name_map['image_company_tax_on_added_value_certificate'],
                    file=files['image_company_tax_on_added_value_certificate'],
                    type=UserMedia
                )
            
        return redirect(reverse_lazy('users:admin_list_buyer'))


class AddLogisticView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/user_management/create_user/create_logistic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES

        with transaction.atomic():
            user = User.objects.create(
                use_type=User.TYPE_LOGISTIC,
                username=data['email'],
                mobile_number=data['mobile_number'],
                email=data['email'],
                legal_type=data['legal_type']
            )

            profile = Profile()
            profile.first_name = data['first_name']
            profile.last_name = data['last_name']
            profile.id_code = data['id_code']
            profile.national_code = data['national_code']
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
            profile.company_license_type = data['company_license_type']
            profile.company_license_code = data['company_license_number']
            profile.company_license_start = data['company_license_start']
            profile.company_license_end = data['company_license_end']
            profile.company_ceo_name = data['company_ceo_name']
            profile.company_ceo_national_code = data['company_ceo_national_code']
            profile.company_ceo_id_code = data['company_ceo_id_code']
            profile.company_branch_type = data['company_branch_type']

            user.save()
            user.profile = profile
            user.profile.save()

            user.media.create(
                title=UserMedia.name_map['image_company_license'],
                file=files['image_company_license'],
                type=UserMedia
            )

            user.media.create(
                title=UserMedia.name_map['image_id_card_front'],
                file=files['image_id_card_front'],
                type=UserMedia
            )

            user.media.create(
                title=UserMedia.name_map['image_id_card_back'],
                file=files['image_id_card_back'],
                type=UserMedia
            )

        return redirect(reverse_lazy('users:admin_list_logistic'))
