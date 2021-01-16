from django.urls import path

from .views import ProductDetailView


app_name = 'products'

urlpatterns = [
    path('1/', ProductDetailView.as_view(), name='product_details')
]
