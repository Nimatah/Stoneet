from django.urls import path

from .views import ProductDetailView, ListProductView, BuyProductView


app_name = 'products'

urlpatterns = [
    path('', ListProductView.as_view(), name='list_products'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('order/1', BuyProductView.as_view(), name='buy_product'),
]
