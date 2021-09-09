from django.urls import path

from apps.users.api.views import (
    SellerAddProductPart1ValidationAPIView,
    RegistrationAuthValidationView,
    MineListCreateAPIView,
    MineRetrieveUpdateDestroyView,
    AddressListCreateAPIView,
    AddressRetrieveUpdateDestroyView,
    UserListAPIView,
    register_buyer_validation,
    register_seller_validation,
    register_logistic_validation,
    user_accept,
    user_reject,
    remove_image,
)

app_name = 'users'

urlpatterns = [
    path('validate/add-product/p1', SellerAddProductPart1ValidationAPIView.as_view(), name='validate_add_seller_part_1'),
    path('validate/registration/auth', RegistrationAuthValidationView.as_view(), name='validate_registration_auth'),
    path('validate/registration/buyer', register_buyer_validation, name='validate_buyer'),
    path('validate/registration/seller', register_seller_validation, name='validate_seller'),
    path('validate/registration/logistic', register_logistic_validation, name='validate_logistic'),
    path('mine/', MineListCreateAPIView.as_view(), name='mine_list_create'),
    path('mine/<int:pk>', MineRetrieveUpdateDestroyView.as_view(), name='mine_detail'),
    path('address/', AddressListCreateAPIView.as_view(), name='address_list_create'),
    path('address/<int:pk>', AddressRetrieveUpdateDestroyView.as_view(), name='address_detail'),
    path('users/', UserListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/accept', user_accept, name='user_accept'),
    path('users/<int:pk>/reject', user_reject, name='user_reject'),
    path('users/remove-image', remove_image, name='remove_image'),
]
