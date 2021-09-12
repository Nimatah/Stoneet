from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from .models import Auction
from apps.orders.models import LogisticOrder
from apps.invoices.models import Invoice


@db_periodic_task(crontab(hour="1/*"))
def process_auction():
    auctions = Auction.objects.find_ready_to_finish()
    for auction in auctions:
        winner_bid = auction.bids.get_lowest_price()
        if not winner_bid:
            auction.set_state_expired()
        else:
            auction.set_state_in_progress(winner_bid)
            logistic_order = LogisticOrder.objects.create(
                order=auction.order,
                state=LogisticOrder.STATE_PENDING,
                user=auction.winner,
                price=winner_bid.price,
                source=auction.order.product.mine,
                destination=auction.order.destination,
                monthly_load_count=auction.order.monthly_load,
                weight=auction.order.weight,
            )
            auction.order.logistic_order = logistic_order
            auction.order.state = auction.order.STATE_LOGISTIC
            auction.order.save()
            Invoice.objects.create(
                user=logistic_order.order.product.user,
                order=logistic_order.order,
                auction=auction,
                state=Invoice.STATE_PRE,
                type=Invoice.TYPE_SELLER,
                price=auction.order.price,
                vat_price=auction.order.price * (Invoice.VAT / 100),
                final_price=auction.order.price + (auction.order.price * (Invoice.VAT / 100)),
            )
            Invoice.objects.create(
                user=logistic_order.order.buyer,
                order=logistic_order.order,
                auction=auction,
                state=Invoice.STATE_PRE,
                type=Invoice.TYPE_BUYER,
                price=auction.order.price,
                vat_price=auction.order.price * (Invoice.VAT / 100),
                final_price=auction.order.price + (auction.order.price * (Invoice.VAT / 100)),
            )
            Invoice.objects.create(
                user=logistic_order.user,
                order=auction.order,
                logistic_order=logistic_order,
                auction=auction,
                state=Invoice.STATE_PRE,
                type=Invoice.TYPE_LOGISTIC,
                price=logistic_order.price,
                vat_price=logistic_order.price * (9 / 100),
                final_price=logistic_order.price + (logistic_order.price * (Invoice.VAT / 100))
            )
