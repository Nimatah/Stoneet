from django.urls import path

from .views import ProductDetailView, ListProductView


app_name = 'products'

urlpatterns = [
    path('', ListProductView.as_view(), name='list_products'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_details'),
]
