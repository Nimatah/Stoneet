from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.auction.models import Auction
from apps.orders.models import Order


class ListAuctionView(UserPassesTestMixin, ListView):

    template_name = 'users/logistic/auction/list_auction.html'
    paginate_by = 10
    context_object_name = 'auctions'
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = Auction.objects.filter(order__state=Order.STATE_PENDING)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_logistic or self.request.user.is_superuser)
