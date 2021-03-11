from django.urls import path

from apps.products.api.views import ListAPIView

app_name = 'products'


urlpatterns = [
    path('products', ListAPIView.as_view(), name='product_view'),
]
