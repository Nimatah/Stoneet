from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.users.views import (
    LoginView,
    RegisterView,
    UserPanelView,
    AddProductView,
    ListProductView,
    EditProductView
)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('panel/dashboard/', UserPanelView.as_view(), name="user_panel"),
    path('panel/add-product/', AddProductView.as_view(), name="add_product"),
    path('panel/list-product/', ListProductView.as_view(), name="list_product"),
    path('panel/edit-product/', EditProductView.as_view(), name='edit_product'),
]
