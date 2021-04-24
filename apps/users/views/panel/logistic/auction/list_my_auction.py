from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q

from apps.auction.models import Bid, Auction


class ListMyAuctionView(UserPassesTestMixin, TemplateView):

    template_name = 'users/logistic/auction/list_my_auction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['in_progress'] = Auction.objects.user_participated_auction(self.request.user).filter(state=Auction.STATE_STARTED)
        context['winner'] = Auction.objects.filter(winner=self.request.user, state=Auction.STATE_IN_PROGRESS)
        context['loser'] = Auction.objects.user_participated_auction(self.request.user).filter(~Q(state=Auction.STATE_STARTED), bids__winner=False)
        context['finished'] = Auction.objects.user_participated_auction(self.request.user).filter(state=Auction.STATE_FINISHED)
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_logistic or self.request.user.is_superuser)
