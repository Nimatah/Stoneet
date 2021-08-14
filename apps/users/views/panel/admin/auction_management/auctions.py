from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.auction.models import Auction
from apps.auction.filters import AdminAuctionFilter


class AdminAuctionView(UserPassesTestMixin, ListView):

    template_name = 'users/admin/auction_management/auctions.html'
    model = Auction
    context_object_name = 'auctions'
    paginate_by = 10
    page_kwarg = 'p'

    def get_queryset(self):
        queryset = Auction.objects.all().order_by('-start_date')
        queryset = AdminAuctionFilter(self.request.GET, queryset=queryset).qs
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
