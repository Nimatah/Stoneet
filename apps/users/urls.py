from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.users.views import (
    LoginView,
    RegisterView,
    UserDashboardView,
    AddProductView,
    ListProductView,
    EditProductView,
    ViewProductView,
)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('panel/dashboard/', UserDashboardView.as_view(), name="dashboard"),
    path('panel/add-product/', AddProductView.as_view(), name="add_product"),
    path('panel/list-product/', ListProductView.as_view(), name="list_product"),
    path('panel/edit-product/<int:pk>', EditProductView.as_view(), name='edit_product'),
    path('panel/view-product/<int:pk>', ViewProductView.as_view(), name='view_product'),
]
