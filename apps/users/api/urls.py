from django.urls import path

from apps.users.api.views import (
    SellerAddProductPart1ValidationAPIView,
    RegistrationAuthValidationView
)

app_name = 'users'

urlpatterns = [
    path('validate/add-product/p1', SellerAddProductPart1ValidationAPIView.as_view(), name='validate_add_seller_part_1'),
    path('validate/registration/auth', RegistrationAuthValidationView.as_view(), name='validate_registration_auth'),
]
