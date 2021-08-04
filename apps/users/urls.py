from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.users.views import auth, password
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
    path('reset-password', password.ResetPasswordView.as_view(), name='reset_password'),
    path('password-confirmation', password.PasswordConfirmationView.as_view(), name='password_confirmation'),
]

seller_patterns = [
    path('panel/superuser-dashboard/', seller.SellerDashboardView.as_view(), name="superuser_dashboard"),
    path('panel/seller-dashboard/', seller.SellerDashboardView.as_view(), name="seller_dashboard"),
    path('panel/new-product/', seller.AddProductView.as_view(), name="seller_add_product"),
    path('panel/list-product/', seller.ListProductView.as_view(), name="seller_list_product"),
    path('panel/edit-product/<int:pk>/', seller.EditProductView.as_view(), name='seller_edit_product'),
    path('panel/product/<int:pk>/', seller.ViewProductView.as_view(), name='seller_view_product'),
    path('panel/seller-orders/', seller.ListOrderView.as_view(), name='seller_list_order'),
    path('panel/seller-order/<int:pk>/', seller.ViewOrderView.as_view(), name='seller_view_order'),
    path('panel/seller-invoices/', seller.ListInvoiceView.as_view(), name='seller_list_invoice'),
    path('panel/seller-invoice/<int:pk>/', seller.ViewInvoiceView.as_view(), name='seller_view_invoice'),
    path('panel/seller-sample-list/', seller.SellerSampleListView.as_view(), name='seller_sample_list'),
    path('panel/seller-sample-detail/', seller.SellerSampleDetailView.as_view(), name='seller_sample_detail'),
]

buyer_patterns = [
    path('panel/buyer-dashboard/', buyer.BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('panel/buyer-orders/', buyer.ListOrderView.as_view(), name='buyer_list_order'),
    path('panel/buyer-order/<int:pk>/', buyer.ViewOrderView.as_view(), name='buyer_view_order'),
    path('panel/buyer-invoices/', buyer.ListInvoiceView.as_view(), name='buyer_list_invoice'),
    path('panel/buyer-invoice/<int:pk>/', buyer.ViewInvoiceView.as_view(), name='buyer_view_invoice'),
    path('panel/buyer-smaple-list/', buyer.BuyerSampleListView.as_view(), name='buyer_sample_list'),
    path('panel/buyer-sample-detail/', buyer.BuyerSampleDetailView.as_view(), name='buyer_sample_detail'),
]

logistic_patterns = [
    path('panel/logistic-dashboard/', logistic.LogisticDashboardView.as_view(), name='logistic_dashboard'),
    path('panel/auctions/', logistic.ListAuctionView.as_view(), name='logistic_list_auction'),
    path('panel/bids/', logistic.ListMyAuctionView.as_view(), name='logistic_list_bid'),
    path('panel/bids/1/', logistic.ViewBidView.as_view(), name='logistic_view_bid'),
    path('panel/logistic-invoices/', logistic.ListInvoiceView.as_view(), name='logistic_list_invoice'),
    path('panel/logistic-invoice/<int:pk>/', logistic.ViewInvoiceView.as_view(), name='logistic_view_invoice'),
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
    path('panel/admin-qc-seller-details/<int:pk>/', admin.QCSellerDetailView.as_view(), name='admin_qc_seller_details'),
    path('panel/admin-qc-logistic-details/<int:pk>/', admin.QCLogisticDetailView.as_view(), name='admin_qc_logistic_details'),
    path('panel/admin-qc-buyer-details/<int:pk>/', admin.QCBuyerDetailView.as_view(), name='admin_qc_buyer_details'),
    path('panel/admin-add-product/', admin.AddProductView.as_view(), name='admin_add_product'),
    path('panel/admin-list-product/', admin.ListProductView.as_view(), name='admin_list_product'),
    path('panel/admin-qc-product-details/<int:pk>/', admin.QCProductDetailsView.as_view(), name='admin_qc_product_details'),
    path('panel/admin-add-category/', admin.AddCategoryView.as_view(), name='admin_add_category'),
    path('panel/admin-edit-category/<int:pk>', admin.edit_category, name='admin_edit_category'),
    path('panel/admin-list-category/', admin.ListCategoryView.as_view(), name='admin_list_category'),
    path('panel/admin-list-auction/', admin.AdminAuctionView.as_view(), name='admin_list_auction'),
    path('panel/admin-auction-details/1/', admin.AdminAuctionDetailsView.as_view(), name='admin_auction_details'),
    path('panel/admin-list-samples', admin.AdminSampleView.as_view(), name='admin_list_samples'),
    path('panel/admin-sample-details/1/', admin.AdminSampleDetailsView.as_view(), name='admin_sample_details'),
    path('panel/admin-list-orders/', admin.AdminOrdersView.as_view(), name='admin_list_order'),
    path('panel/admin-order-qc/<int:pk>/', admin.AdminOrderQCView.as_view(), name='admin_order_qc'),
    path('panel/admin-configurations/', admin.AdminConfigView.as_view(), name='admin_config'),
    path('panel/admin-list-buyer-invoice/', admin.AdminBuyerInvoiceView.as_view(), name='admin_list_buyer_invoice'),
    path('panel/admin-buyer-invoice-details/<int:pk>/', admin.AdminBuyerInvoiceDetailsView.as_view(), name='admin_buyer_invoice_details'),
    path('panel/admin-list-seller-invoice/', admin.AdminSellerInvoiceView.as_view(), name='admin_list_seller_invoice'),
    path('panel/admin-seller-invoice-details/<int:pk>/', admin.AdminSellerInvoiceDetailsView.as_view(), name='admin_seller_invoice_details'),
    path('panel/admin-list-logistic-invoice/', admin.AdminLogisticInvoiceView.as_view(), name='admin_list_logistic_invoice'),
    path('panel/admin-logistic-invoice-details/<int:pk>/', admin.AdminLogisticInvoiceDetailsView.as_view(), name='admin_logistic_invoice_details'),
    path('panel/admin-logistic-orders/', admin.AdminLogisticOrdersView.as_view(), name='admin_logistic_orders'),
    path('panel/admin-logistic-order-details/<int:pk>', admin.AdminLogisticOrderQCView.as_view(), name='admin_logistic_order_qc'),
    path('panel/admin-sample-list/', admin.AdminSampleListView.as_view(), name='admin_sample_list'),
    path('panel/admin-sample-detail/', admin.AdminSampleDetailView.as_view(), name='admin_sample_detail'),
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
