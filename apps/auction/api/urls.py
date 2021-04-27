from django.urls import path

from .views import get_auction, create_bid, get_auction_admin, reactivate_auction

app_name = 'auctions'


urlpatterns = [
    path('auctions/<int:pk>', get_auction, name='get_auction'),
    path('auctions/<int:pk>/bid', create_bid, name='create_bid'),
    path('auctions/<int:pk>/admin', get_auction_admin, name='get_auction_admin'),
    path('auctions/<int:pk>/admin/reactivate', reactivate_auction, name='reactivate_auction'),
]
