from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from persiantools.jdatetime import JalaliDate

from apps.users.models import User, UserMedia
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

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES
        user = User.objects.get(pk=kwargs['pk'])

        if data.get('legal_type') == User.LEGAL_INDIVIDUAL:
            with transaction.atomic():

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
                user.profile.bank_account_name = data['bank_account_name']
                user.profile.bank_account_number = data['bank_account_number']
                user.profile.bank_sheba_number = data['bank_sheba_number']

                user.save()
                user.profile.save()

                image_id_card_front = user.media.filter(
                    title=UserMedia.name_map['image_id_card_front']
                ).first()

                if image_id_card_front:
                    if files.get('image_id_card_front'):
                        image_id_card_front.file = files['image_id_card_front']
                        image_id_card_front.save()
                else:
                    if files.get('image_id_card_front'):
                        user.media.create(
                            title=UserMedia.name_map['image_id_card_front'],
                            file=files['image_id_card_front'],
                            type=UserMedia.TYPE_IMAGE
                        )

                image_id_card_back = user.media.filter(
                    title=UserMedia.name_map['image_id_card_back']
                ).first()

                if image_id_card_back:
                    if files.get('image_id_card_back'):
                        image_id_card_back.file = files['image_id_card_back']
                        image_id_card_back.save()
                else:
                    if files.get('image_id_card_back'):
                        user.media.create(
                            title=UserMedia.name_map['image_id_card_back'],
                            file=files['image_id_card_back'],
                            type=UserMedia.TYPE_IMAGE
                        )

        else:
            with transaction.atomic():
                user.email = data['email']
                user.mobile_number = data['mobile_number']

                user.profile.address = data['address']
                user.profile.postal_code = data['postal_code']
                user.profile.region_id = data['region']
                user.profile.phone_number = data['phone_number']
                user.profile.bank_account_name = data['bank_account_name']
                user.profile.bank_account_number = data['bank_account_number']
                user.profile.bank_sheba_number = data['bank_sheba_number']
                user.profile.company_name = data['company_name']
                user.profile.company_type = data['company_type']
                user.profile.company_register_code = data['company_register_code']
                user.profile.company_national_code = data['company_national_code']
                user.profile.company_finance_code = data['company_finance_code']
                user.profile.company_print_signature_right = data['company_print_signature_right']

                user.save()
                user.profile.save()

                image_company_registration = user.media.filter(
                    title=UserMedia.name_map['image_company_registration']
                ).first()

                if image_company_registration:
                    if files.get('image_company_registration'):
                        image_company_registration.file = files['image_company_registration']
                        image_company_registration.save()
                else:
                    if files.get('image_company_registration'):
                        user.media.create(
                            title=UserMedia.name_map['image_company_registration'],
                            file=files['image_company_registration'],
                            type=UserMedia.TYPE_IMAGE
                        )

                image_company_latest_newspaper = user.media.filter(
                    title=UserMedia.name_map['image_company_latest_newspaper']
                ).first()

                if image_company_latest_newspaper:
                    if files.get('image_company_latest_newspaper'):
                        image_company_latest_newspaper.file = files['image_company_latest_newspaper']
                        image_company_latest_newspaper.save()
                else:
                    if files.get('image_company_latest_newspaper'):
                        user.media.create(
                            title=UserMedia.name_map['image_company_latest_newspaper'],
                            file=files['image_company_latest_newspaper'],
                            type=UserMedia.TYPE_IMAGE
                        )

                image_company_tax_on_added_value_certificate = user.media.filter(
                    title=UserMedia.name_map['image_company_tax_on_added_value_certificate']
                ).first()

                if image_company_tax_on_added_value_certificate:
                    if files.get('image_company_tax_on_added_value_certificate'):
                        image_company_tax_on_added_value_certificate.file = files[
                            'image_company_tax_on_added_value_certificate']
                        image_company_tax_on_added_value_certificate.save()
                else:
                    if files.get('image_company_tax_on_added_value_certificate'):
                        user.media.create(
                            title=UserMedia.name_map['image_company_tax_on_added_value_certificate'],
                            file=files['image_company_tax_on_added_value_certificate'],
                            type=UserMedia.TYPE_IMAGE
                        )

        return redirect(reverse_lazy('users:admin_list_seller'))


class EditBuyerView(DetailView):
    template_name = 'users/admin/user_management/edit_user/edit_buyer.html'
    model = User
    context_object_name = 'buyer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES
        user = User.objects.get(pk=kwargs['pk'])

        if data.get('legal_type') == User.LEGAL_INDIVIDUAL:
            with transaction.atomic():

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
                user.profile.bank_account_name = data['bank_account_name']
                user.profile.bank_account_number = data['bank_account_number']
                user.profile.bank_sheba_number = data['bank_sheba_number']

                user.save()
                user.profile.save()

                image_id_card_front = user.media.filter(
                    title=UserMedia.name_map['image_id_card_front']
                ).first()

                if image_id_card_front:
                    if files.get('image_id_card_front'):
                        image_id_card_front.file = files['image_id_card_front']
                        image_id_card_front.save()
                else:
                    if files.get('image_id_card_front'):
                        user.media.create(
                            title=UserMedia.name_map['image_id_card_front'],
                            file=files['image_id_card_front'],
                            type=UserMedia.TYPE_IMAGE
                        )

                image_id_card_back = user.media.filter(
                    title=UserMedia.name_map['image_id_card_back']
                ).first()

                if image_id_card_back:
                    if files.get('image_id_card_back'):
                        image_id_card_back.file = files['image_id_card_back']
                        image_id_card_back.save()
                else:
                    if files.get('image_id_card_back'):
                        user.media.create(
                            title=UserMedia.name_map['image_id_card_back'],
                            file=files['image_id_card_back'],
                            type=UserMedia.TYPE_IMAGE
                        )

        else:
            with transaction.atomic():
                user.email = data['email']
                user.mobile_number = data['mobile_number']

                user.profile.address = data['address']
                user.profile.postal_code = data['postal_code']
                user.profile.region_id = data['region']
                user.profile.phone_number = data['phone_number']
                user.profile.bank_account_name = data['bank_account_name']
                user.profile.bank_account_number = data['bank_account_number']
                user.profile.bank_sheba_number = data['bank_sheba_number']
                user.profile.company_name = data['company_name']
                user.profile.company_type = data['company_type']
                user.profile.company_register_code = data['company_register_code']
                user.profile.company_national_code = data['company_national_code']
                user.profile.company_finance_code = data['company_finance_code']
                user.profile.company_print_signature_right = data['company_print_signature_right']

                user.save()
                user.profile.save()

                image_company_registration = user.media.filter(
                    title=UserMedia.name_map['image_company_registration']
                ).first()

                if image_company_registration:
                    if files.get('image_company_registration'):
                        image_company_registration.file = files['image_company_registration']
                        image_company_registration.save()
                else:
                    if files.get('image_company_registration'):
                        user.media.create(
                            title=UserMedia.name_map['image_company_registration'],
                            file=files['image_company_registration'],
                            type=UserMedia.TYPE_IMAGE
                        )

                image_company_latest_newspaper = user.media.filter(
                    title=UserMedia.name_map['image_company_latest_newspaper']
                ).first()

                if image_company_latest_newspaper:
                    if files.get('image_company_latest_newspaper'):
                        image_company_latest_newspaper.file = files['image_company_latest_newspaper']
                        image_company_latest_newspaper.save()
                else:
                    if files.get('image_company_latest_newspaper'):
                        user.media.create(
                            title=UserMedia.name_map['image_company_latest_newspaper'],
                            file=files['image_company_latest_newspaper'],
                            type=UserMedia.TYPE_IMAGE
                        )

                image_company_tax_on_added_value_certificate = user.media.filter(
                    title=UserMedia.name_map['image_company_tax_on_added_value_certificate']
                ).first()

                if image_company_tax_on_added_value_certificate:
                    if files.get('image_company_tax_on_added_value_certificate'):
                        image_company_tax_on_added_value_certificate.file = files['image_company_tax_on_added_value_certificate']
                        image_company_tax_on_added_value_certificate.save()
                else:
                    if files.get('image_company_tax_on_added_value_certificate'):
                        user.media.create(
                            title=UserMedia.name_map['image_company_tax_on_added_value_certificate'],
                            file=files['image_company_tax_on_added_value_certificate'],
                            type=UserMedia.TYPE_IMAGE
                        )

        return redirect(reverse_lazy('users:admin_list_buyer'))


class EditLogisticView(DetailView):
    template_name = 'users/admin/user_management/edit_user/edit_logistic.html'
    model = User
    context_object_name = 'logistic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES

        with transaction.atomic():
            user = User.objects.get(pk=kwargs['pk'])

            user.profile.first_name = data['first_name']
            user.profile.last_name = data['last_name']
            user.profile.id_code = data['id_code']
            user.profile.national_code = data['national_code']
            user.profile.address = data['address']
            user.profile.postal_code = data['postal_code']
            user.profile.region_id = data['region']
            user.profile.phone_number = data['phone_number']
            user.profile.bank_account_name = data['bank_account_name']
            user.profile.bank_account_number = data['bank_account_number']
            user.profile.bank_sheba_number = data['bank_sheba_number']
            user.profile.company_name = data['company_name']
            user.profile.company_type = data['company_type']
            user.profile.company_register_code = data['company_register_code']
            user.profile.company_license_type = data['company_license_type']
            user.profile.company_license_code = data['company_license_code']
            user.profile.company_license_start = data['company_license_start']
            user.profile.company_license_end = data['company_license_end']
            user.profile.company_ceo_name = data['company_ceo_name']
            user.profile.company_ceo_national_code = data['company_ceo_national_code']
            user.profile.company_ceo_id_code = data['company_ceo_id_code']
            user.profile.company_branch_type = data['company_branch_type']

            user.save()
            user.profile.save()

            image_company_license = user.media.filter(
                title=UserMedia.name_map['image_company_license']
            ).first()

            if image_company_license:
                if files.get('image_company_license'):
                    image_company_license.file = files['image_company_license']
                    image_company_license.save()
            else:
                if files.get('image_company_license'):
                    user.media.create(
                        title=UserMedia.name_map['image_company_license'],
                        file=files['image_company_license'],
                        type=UserMedia.TYPE_IMAGE
                    )

            image_id_card_front = user.media.filter(
                title=UserMedia.name_map['image_id_card_front']
            ).first()

            if image_id_card_front:
                if files.get('image_id_card_front'):
                    image_company_license.file = files['image_id_card_front']
                    image_company_license.save()
            else:
                if files.get('image_id_card_front'):
                    user.media.create(
                        title=UserMedia.name_map['image_id_card_front'],
                        file=files['image_id_card_front'],
                        type=UserMedia.TYPE_IMAGE
                    )

            image_id_card_back = user.media.filter(
                title=UserMedia.name_map['image_id_card_back']
            ).first()

            if image_id_card_back:
                if files.get('image_id_card_back'):
                    image_company_license.file = files['image_id_card_back']
                    image_company_license.save()
            else:
                if files.get('image_id_card_back'):
                    user.media.create(
                        title=UserMedia.name_map['image_id_card_back'],
                        file=files['image_id_card_back'],
                        type=UserMedia.TYPE_IMAGE
                    )

        return redirect(reverse_lazy('users:admin_list_logistic'))
