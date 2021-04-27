from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from .models import Auction


@db_periodic_task(crontab(hour="1/*"))
def process_auction():
    auctions = Auction.objects.find_ready_to_finish()
    for auction in auctions:
        winner_bid = auction.bids.get_lowest_price()
        if not winner_bid:
            auction.set_state_expired()
        else:
            auction.set_state_in_progress(winner_bid)
