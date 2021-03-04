from django.views.generic import TemplateView


class AdminAuctionDetailsView(TemplateView):
    template_name = 'users/admin/auction_management/auction_details.html'
