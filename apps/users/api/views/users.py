from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ..serializers.users import UserSerializer
from ...models import User, UserMedia


class UserListAPIView(ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        query = {'use_type': User.TYPE_SELLER}
        seller_id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        mobile_number = self.request.query_params.get('mobile_number', None)
        if seller_id is not None:
            query.update({'id': seller_id})
        if mobile_number is not None:
            query.update({'mobile_number': mobile_number})
        if name is not None:
            query.update({'profile__full_name__icontains': name})
        return User.objects.filter(**query)


@api_view(['POST', ])
def register_seller_validation(request):
    errors = {}
    data = request.data
    if not data.get('legal_type'):
        errors['نوع کاربری'] = 'لطفا نوع کاربر حقیقی یا حقوقی را وارد نمایید'
    if data.get('legal_type') == 'legal':
        if not data.get('company_type'):
            errors['نوع شرکت'] = 'لطفا نوع شرکت را انتخاب کنید'
        if not data.get('company_name'):
            errors['نام شرکت'] = 'لطفا نام شرکت را وارد نمایید'
        if not data.get('address'):
            errors['آدرس'] = 'لطفا آدرس را وارد نمایید'
        if not data.get('company_register_code'):
            errors['شماره ثبت'] = 'لطفا شماره ثبت را واید نمایید'
        if not data.get('company_ceo_name'):
            errors['نام مدیر عامل'] = 'لطفا نام مدیر عامل را وارد نمایید'
        if not data.get('phone_number'):
            errors['تلفن ثابت'] = 'لطفا تلفن ثابت را وارد نمایید'
    elif data['legal_type'] == 'individual':
        if not data.get('first_name'):
            errors['نام'] = 'لطفا نام را وارد نمایید'
        if not data.get('last_name'):
            errors['نام خانوادگی'] = 'لطفا نام خانوادگی را وارد نمایید'
        if not data.get('phone_number'):
            errors['تلفن ثابت'] = 'لطفا تلفن ثابت را وارد نمایید'
        if not data.get('national_code'):
            errors['کد ملی'] = 'لطفا کد ملی را وارد نمایید'
        if not data.get('address'):
            errors['آدرس'] = 'لطفا آدرس را وارد نمایید'
    if errors:
        return Response(errors, status=400)
    return Response(None, status=200)


@api_view(['POST', ])
def register_buyer_validation(request):
    errors = {}
    data = request.data
    if not data.get('legal_type'):
        errors['نوع کاربری'] = 'لطفا نوع کاربر حقیقی یا حقوقی را وارد نمایید'
    if data.get('legal_type') == 'legal':
        if not data.get('company_type'):
            errors['نوع شرکت'] = 'لطفا نوع شرکت را انتخاب کنید'
        if not data.get('company_name'):
            errors['نام شرکت'] = 'لطفا نام شرکت را وارد نمایید'
        if not data.get('address'):
            errors['آدرس'] = 'لطفا آدرس را وارد نمایید'
        if not data.get('company_register_code'):
            errors['شماره ثبت'] = 'لطفا شماره ثبت را واید نمایید'
        if not data.get('company_ceo_name'):
            errors['نام مدیر عامل'] = 'لطفا نام مدیر عامل را وارد نمایید'
        if not data.get('phone_number'):
            errors['تلفن ثابت'] = 'لطفا تلفن ثابت را وارد نمایید'
    elif data['legal_type'] == 'individual':
        if not data.get('first_name'):
            errors['نام'] = 'لطفا نام را وارد نمایید'
        if not data.get('last_name'):
            errors['نام خانوادگی'] = 'لطفا نام خانوادگی را وارد نمایید'
        if not data.get('phone_number'):
            errors['تلفن ثابت'] = 'لطفا تلفن ثابت را وارد نمایید'
        if not data.get('national_code'):
            errors['کد ملی'] = 'لطفا کد ملی را وارد نمایید'
        if not data.get('address'):
            errors['آدرس'] = 'لطفا آدرس را وارد نمایید'
    if errors:
        return Response(errors, status=400)
    return Response(None, status=200)


@api_view(['POST', ])
def register_logistic_validation(request):
    errors = {}
    data = request.data

    if not data.get('company_name'):
        errors['نام شرکت'] = 'لطفا نام شرکت را وارد نمایید'
    if not data.get('company_type'):
        errors['نوع شرکت'] = 'لطفا نوع شرکت را انتخاب کنید'
    if not data.get('company_license_type'):
        errors['نوع پروانه شرکت'] = 'لطفا نوع پروانه شرکت را انتخاب نمایید'
    if not data.get('company_license_code'):
        errors['شماره پروانه شرکت'] = 'لطفا شماره پروانه شرکت را وارد نمایید'
    if not data.get('company_ceo_name'):
        errors['نام مدیر عامل شرکت'] = 'لطفا نام مدیر عامل شرکت را وارد نمایید'
    if data.get('company_branch') == 'انتخاب کنید:':
        if not data.get('first_name'):
            errors['نام'] = 'لطفا نام را وارد نمایید'
        if not data.get('last_name'):
            errors['نام خانوادگی'] = 'لطفا نام خانوادگی را وارد نمایید'
        if not data.get('phone_number'):
            errors['تلفن ثابت'] = 'لطفا تلفن ثابت را وارد نمایید'
        if not data.get('national_code'):
            errors['کد ملی'] = 'لطفا کد ملی را وارد نمایید'
        if not data.get('address'):
            errors['آدرس'] = 'لطفا آدرس را وارد نمایید'

    if errors:
        return Response(errors, status=400)
    return Response(None, status=200)


@api_view(['GET', ])
def user_accept(request, pk):
    if not request.user.is_authenticated and not (request.user.is_admin or request.user.is_superuser):
        return Response({'error': 'شما دسترسی ندارید'}, status=401)

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'کاربر پیدا نشد'}, status=404)

    user.state = User.STATE_ACCEPTED
    user.rejection_reason = ''
    user.save()

    return Response('', status=200)


@api_view(['GET', ])
def user_reject(request, pk):
    if not request.user.is_authenticated and not (request.user.is_admin or request.user.is_superuser):
        return Response({'error': 'شما دسترسی ندارید'}, status=401)

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'کاربر پیدا نشد'}, status=404)

    user.state = User.STATE_REJECTED
    user.rejection_reason = request.query_params.get('reason')
    user.save()

    return Response('', status=200)


@api_view(['DELETE', ])
def remove_image(request: Request):
    pk = request.query_params.get('pk', None)

    if not request.user.is_authenticated or not (request.user.is_admin or request.user.is_superuser):
        return Response({'error': 'شما دسترسی ندارید'}, status=400)

    if pk is None:
        return Response({'error': 'name or pk is required'}, status=400)
    else:
        media = UserMedia.objects.get(pk=pk)
        media.delete()
        return Response('', status=204)
