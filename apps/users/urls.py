from django.urls import path
from django.contrib.auth.views import LogoutView


from apps.users.views import auth
from apps.users.views.panel import seller, buyer, logistic

app_name = 'users'

urlpatterns = [
    path('register/', auth.RegisterView.as_view(), name='register'),
    path('login/', auth.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('panel/dashboard/', auth.LoginRedirectView.as_view(), name='redirect'),

    path('panel/superuser-dashboard/', seller.SellerDashboardView.as_view(), name="superuser_dashboard"),

    path('panel/seller-dashboard/', seller.SellerDashboardView.as_view(), name="seller_dashboard"),
    path('panel/new-product/', seller.AddProductView.as_view(), name="seller_add_product"),
    path('panel/list-product/', seller.ListProductView.as_view(), name="seller_list_product"),
    path('panel/edit-product/<int:pk>/', seller.EditProductView.as_view(), name='seller_edit_product'),
    path('panel/product/<int:pk>/', seller.ViewProductView.as_view(), name='seller_view_product'),
    path('panel/seller-orders/', seller.ListOrderView.as_view(), name='seller_list_order'),
    path('panel/seller-order/1/', seller.ViewOrderView.as_view(), name='seller_view_order'),
    path('panel/seller-invoices/', seller.ListInvoiceView.as_view(), name='seller_list_invoice'),
    path('panel/seller-invoice/1/', seller.ViewInvoiceView.as_view(), name='seller_view_invoice'),

    path('panel/buyer-dashboard/', buyer.BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('panel/buyer-orders/', buyer.ListOrderView.as_view(), name='buyer_list_order'),
    path('panel/buyer-order/1/', buyer.ViewOrderView.as_view(), name='buyer_view_order'),
    path('panel/buyer-invoices/', buyer.ListInvoiceView.as_view(), name='buyer_list_invoice'),
    path('panel/buyer-invoice/1/', buyer.ViewInvoiceView.as_view(), name='buyer_view_invoice'),
    path('panel/buyer-receipts/', buyer.ListReceiptView.as_view(), name='buyer_list_receipt'),

    path('panel/logistic-dashboard/', logistic.LogisticDashboardView.as_view(), name='logistic_dashboard'),
    path('panel/auctions/', logistic.ListAuctionView.as_view(), name='logistic_list_auction'),
    path('panel/bids/', logistic.ListMyBidView.as_view(), name='logistic_list_bid'),
    path('panel/bids/1/', logistic.ViewBidView.as_view(), name='logistic_view_bid'),
    path('panel/logistic-invoices/', logistic.ListInvoiceView.as_view(), name='logistic_list_invoice'),
    path('panel/logistic-invoice/1/', logistic.ViewInvoiceView.as_view(), name='logistic_view_invoice'),
    path('panel/logistic-orders/', logistic.ListLogisticOrderView.as_view(), name='logistic_list_order'),
    path('panel/logistic-order/1/', logistic.ViewLogisticOrderView.as_view(), name='logistic_view_order'),
]
