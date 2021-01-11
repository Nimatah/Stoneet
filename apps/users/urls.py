from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.users.views import auth
from apps.users.views.panel import seller, buyer

app_name = 'users'

urlpatterns = [
    path('register/', auth.RegisterView.as_view(), name='register'),
    path('login/', auth.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('panel/seller/dashboard/', seller.SellerDashboardView.as_view(), name="seller_dashboard"),
    path('panel/seller/products/new', seller.AddProductView.as_view(), name="seller_add_product"),
    path('panel/seller/products/', seller.ListProductView.as_view(), name="seller_list_product"),
    path('panel/seller/products/edit/<int:pk>', seller.EditProductView.as_view(), name='seller_edit_product'),
    path('panel/seller/products/<int:pk>', seller.ViewProductView.as_view(), name='seller_view_product'),
    path('panel/seller/orders/', seller.ListOrderView.as_view(), name='seller_list_order'),
    path('panel/seller/orders/<int:pk>', seller.ViewOrderView.as_view(), name='seller_view_order'),

    path('panel/buyer/dashboard/', buyer.BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('panel/buyer/orders/', buyer.ListOrderView.as_view(), name='buyer_list_order'),
    path('panel/buyer/orders/<int:pk>', buyer.ViewOrderView.as_view(), name='buyer_view_order'),
]
