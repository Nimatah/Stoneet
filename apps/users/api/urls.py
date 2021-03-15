from django.urls import path

from apps.users.api.views import (
    SellerAddProductPart1ValidationAPIView,
    RegistrationAuthValidationView,
    MineListCreateAPIView,
    MineRetrieveUpdateDestroyView,
    AddressListCreateAPIView,
    AddressRetrieveUpdateDestroyView,
    UserListAPIView,
)

app_name = 'users'

urlpatterns = [
    path('validate/add-product/p1', SellerAddProductPart1ValidationAPIView.as_view(), name='validate_add_seller_part_1'),
    path('validate/registration/auth', RegistrationAuthValidationView.as_view(), name='validate_registration_auth'),
    path('mine/', MineListCreateAPIView.as_view(), name='mine_list_create'),
    path('mine/<int:pk>', MineRetrieveUpdateDestroyView.as_view(), name='mine_detail'),
    path('address/', AddressListCreateAPIView.as_view(), name='address_list_create'),
    path('address/<int:pk>', AddressRetrieveUpdateDestroyView.as_view(), name='address_detail'),
    path('users/', UserListAPIView.as_view(), name='user_list')
]
