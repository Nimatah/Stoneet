from django.urls import path

from .views import get_auction, create_bid

app_name = 'auctions'


urlpatterns = [
    path('auctions/<int:pk>', get_auction, name='get_auction'),
    path('auctions/<int:pk>/bid', create_bid, name='create_bid'),
]
