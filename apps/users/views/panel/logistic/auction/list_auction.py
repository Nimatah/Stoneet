from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.auction.models import Auction


class ListAuctionView(UserPassesTestMixin, ListView):
    template_name = 'users/logistic/auction/list_auction.html'
    context_object_name = 'auctions'

    # TODO: Change logistic bid to price per tons

    def get_queryset(self):
        queryset = Auction.objects.filter(state=Auction.STATE_STARTED, order__is_rejected=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_logistic or self.request.user.is_superuser)
