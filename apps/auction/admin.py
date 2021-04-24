from django.contrib import admin

from apps.auction.models import Auction, Bid


class BidInline(admin.StackedInline):

    model = Bid


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):

    inlines = [BidInline, ]
