from django.urls import path

from .views import StaticContentUpdateAPIView

app_name = 'home'

urlpatterns = [
    path('static-content/<int:pk>', StaticContentUpdateAPIView.as_view(), name='static_content_api'),
]
