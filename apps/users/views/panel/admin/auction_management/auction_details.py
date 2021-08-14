from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class AdminAuctionDetailsView(UserPassesTestMixin, TemplateView):
    template_name = 'users/admin/auction_management/auction_details.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
