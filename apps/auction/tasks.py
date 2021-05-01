from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from .models import Auction
from apps.orders.models import LogisticOrder


@db_periodic_task(crontab(hour="1/*"))
def process_auction():
    auctions = Auction.objects.find_ready_to_finish()
    for auction in auctions:
        winner_bid = auction.bids.get_lowest_price()
        if not winner_bid:
            auction.set_state_expired()
        else:
            auction.set_state_in_progress(winner_bid)
            LogisticOrder.objects.create(
                order=auction.order,
                state=LogisticOrder.STATE_PENDING,
                user=auction.winner,
                price=winner_bid.price,
                source=auction.order.product.mine,
                destination=auction.order.destination,
                monthly_load_count=auction.order.monthly_load,
                weight=auction.order.weight,
            )
