from django.urls import path

from .views import OrderFormView, create_sample_order

app_name = 'orders'


urlpatterns = [
    path('create', OrderFormView.as_view(), name='create_order'),
    path('sample', create_sample_order, name='create_sample')
]
