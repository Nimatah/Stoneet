from django.urls import path

from apps.products.api.views import ListAPIView, product_accept, product_reject, remove_image

app_name = 'products'


urlpatterns = [
    path('products/', ListAPIView.as_view(), name='product_view'),
    path('products/<int:pk>/accept', product_accept, name='product_accept'),
    path('products/<int:pk>/reject', product_reject, name='product_reject'),
    path('products/remove-image', remove_image, name='remove_image'),
]
