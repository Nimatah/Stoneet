from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.users.views import auth
from apps.users.views.panel import seller, buyer, logistic, admin

app_name = 'users'

auth_patterns = [
    path('seller-register/', auth.SellerRegisterView.as_view(), name='register_seller'),
    path('buyer-register/', auth.BuyerRegisterView.as_view(), name='register_buyer'),
    path('logistic-register/', auth.LogisticRegisterView.as_view(), name='register_logistic'),
    path('login/', auth.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('seller-profile', seller.SellerProfileView.as_view(), name='profile_seller'),
    path('buyer-profile', buyer.BuyerProfileView.as_view(), name='profile_buyer'),
    path('logistic-profile', logistic.LogisticProfileView.as_view(), name='profile_logistic'),
]

seller_patterns = [
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
]

buyer_patterns = [
    path('panel/buyer-dashboard/', buyer.BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('panel/buyer-orders/', buyer.ListOrderView.as_view(), name='buyer_list_order'),
    path('panel/buyer-order/1/', buyer.ViewOrderView.as_view(), name='buyer_view_order'),
    path('panel/buyer-invoices/', buyer.ListInvoiceView.as_view(), name='buyer_list_invoice'),
    path('panel/buyer-invoice/1/', buyer.ViewInvoiceView.as_view(), name='buyer_view_invoice'),
    path('panel/buyer-receipts/', buyer.ListReceiptView.as_view(), name='buyer_list_receipt'),
]

logistic_patterns = [
    path('panel/logistic-dashboard/', logistic.LogisticDashboardView.as_view(), name='logistic_dashboard'),
    path('panel/auctions/', logistic.ListAuctionView.as_view(), name='logistic_list_auction'),
    path('panel/bids/', logistic.ListMyBidView.as_view(), name='logistic_list_bid'),
    path('panel/bids/1/', logistic.ViewBidView.as_view(), name='logistic_view_bid'),
    path('panel/logistic-invoices/', logistic.ListInvoiceView.as_view(), name='logistic_list_invoice'),
    path('panel/logistic-invoice/1/', logistic.ViewInvoiceView.as_view(), name='logistic_view_invoice'),
    path('panel/logistic-orders/', logistic.ListLogisticOrderView.as_view(), name='logistic_list_order'),
    path('panel/logistic-order/1/', logistic.ViewLogisticOrderView.as_view(), name='logistic_view_order'),
]

admin_patterns = [
    path('panel/admin-dashboard/', admin.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('panel/admin-add-seller/', admin.AddSellerView.as_view(), name='admin_add_seller'),
    path('panel/admin-add-buyer/', admin.AddBuyerView.as_view(), name='admin_add_buyer'),
    path('panel/admin-add-logistic/', admin.AddLogisticView.as_view(), name='admin_add_logistic'),
    path('panel/admin-add-admin/', admin.AddAdminView.as_view(), name='admin_add_admin'),
    path('panel/admin-list-seller/', admin.ListSellerView.as_view(), name='admin_list_seller'),
    path('panel/admin-list-buyer/', admin.ListBuyerView.as_view(), name='admin_list_buyer'),
    path('panel/admin-list-logistic/', admin.ListLogisticView.as_view(), name='admin_list_logistic'),
    path('panel/admin-list-admin/', admin.ListAdminView.as_view(), name='admin_list_admin'),
    path('panel/admin-qc-seller/', admin.QCSellerView.as_view(), name='admin_qc_seller'),
    path('panel/admin-qc-logistic/', admin.QCLogisticView.as_view(), name='admin_qc_logistic'),
]

application_patterns = [
    path('panel/dashboard/', auth.LoginRedirectView.as_view(), name='redirect'),
]

urlpatterns = (
        auth_patterns +
        seller_patterns +
        buyer_patterns +
        logistic_patterns +
        admin_patterns +
        application_patterns
)
