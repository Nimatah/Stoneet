from django.urls import path

from apps.users.api.views.seller import SellerAddProductPart1ValidationAPIView

app_name = 'users'

urlpatterns = [
    path('validate/add-product/p1', SellerAddProductPart1ValidationAPIView.as_view(), name='validate_add_seller_part_1'),
]
