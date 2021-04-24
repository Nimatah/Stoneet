from django.urls import path

from .views import seller_order_accept, seller_order_reject

app_name = 'orders'


urlpatterns = [
    path("orders/<int:pk>/seller-accept", seller_order_accept, name="seller_accept"),
    path("orders/<int:pk>/seller-reject", seller_order_reject, name="seller_reject"),
]
