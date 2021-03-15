from django.urls import path

from .views import OrderFormView

app_name = 'orders'


urlpatterns = [
    path('create', OrderFormView.as_view(), name='create_order')
]
