from datetime import datetime, timedelta

from django.db import models
from persiantools.jdatetime import JalaliDateTime


class AuctionQuerySet(models.QuerySet):

    def user_participated_auction(self, user):
        return self.filter(bids__user=user)


class BidQuerySet(models.QuerySet):

    def get_lowest_price(self):
        return self.filter().order_by('price').first()


class AuctionManager(models.Manager):

    def get_queryset(self) -> 'AuctionQuerySet':
        return AuctionQuerySet(model=self.model, using=self.db)

    def user_participated_auction(self, user):
        return self.filter(bids__user=user)

    def find_ready_to_finish(self):
        return self.filter(state=Auction.STATE_STARTED, finish_date__lt=datetime.now())


class BidManager(models.Manager):

    def get_queryset(self) -> 'BidQuerySet':
        return BidQuerySet(model=self.model, using=self.db)

    def get_lowest_price(self):
        return self.filter().order_by('price').first()


class Auction(models.Model):

    STATE_STARTED = 'started'
    STATE_IN_PROGRESS = 'in_progress'
    STATE_FINISHED = 'finished'
    STATE_EXPIRED = 'expired'

    STATE_CHOICES = (
        (STATE_STARTED, 'شروع شده',),
        (STATE_IN_PROGRESS, 'در حال انجام',),
        (STATE_FINISHED, 'تمام شده',),
        (STATE_EXPIRED, 'منقضی شده',),
    )

    start_date = models.DateTimeField(null=True, blank=True)
    finish_date = models.DateTimeField(null=True, blank=True)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='auctions')
    winner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='auctions', null=True, blank=True)
    state = models.CharField(max_length=255, choices=STATE_CHOICES)

    objects = AuctionManager()

    def winner_bid(self) -> 'Bid':
        try:
            return self.bids.get(winner=True)
        except:
            return None

    def is_completed(self) -> bool:
        return self.bids.filter(winner=True).exists()

    def finish_and_set_winner(self):
        winner_bid: 'Bid' = self.bids.get_lowest_price()
        if not winner_bid:
            self.set_state_expired()
            return
        winner_bid.set_winner()
        self.set_state_in_progress(winner_bid)

    def set_state_in_progress(self, winner_bid: 'Bid'):
        self.state = self.STATE_IN_PROGRESS
        self.winner = winner_bid.user
        self.save()

    def set_state_expired(self):
        self.state = self.STATE_EXPIRED
        self.save()

    def set_state_started(self):
        self.bids.all().delete()
        self.state = self.STATE_STARTED
        self.winner = None
        self.start_date = datetime.now()
        self.finish_date = datetime.now() + timedelta(days=1)
        self.save()

    def get_persian_start_date(self):
        return JalaliDateTime(self.start_date)

    def get_persian_finish_date(self):
        return JalaliDateTime(self.finish_date)

    def has_user_participated(self, user):
        return self.bids.filter(user=user).exists()


class Bid(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    auction = models.ForeignKey('Auction', on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='bids')
    price = models.BigIntegerField(null=True, blank=True)
    winner = models.BooleanField(default=False)

    objects = BidManager()

    def set_winner(self):
        self.winner = True
        self.save()
