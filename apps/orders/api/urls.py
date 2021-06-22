from django.urls import path

from .views import seller_order_accept, seller_order_reject, \
    save_order_contract_images, save_order_finance_images, remove_order_image

app_name = 'orders'


urlpatterns = [
    path("orders/<int:pk>/seller-accept", seller_order_accept, name="seller_accept"),
    path("orders/<int:pk>/seller-reject", seller_order_reject, name="seller_reject"),
    path("orders/<int:pk>/upload-signed", save_order_contract_images, name="upload_signed"),
    path("orders/<int:pk>/upload-finance", save_order_finance_images, name="upload_finance"),
    path("orders/<int:pk>/media/<int:image_pk>/", remove_order_image, name="remove_image"),
]
