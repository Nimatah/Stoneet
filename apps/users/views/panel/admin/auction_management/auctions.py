from django.views.generic import TemplateView


class AdminAuctionView(TemplateView):

    template_name = 'users/admin/auction_management/auctions.html'
