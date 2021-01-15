from django.views.generic import DetailView, TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.auction.models import Bid


class ViewBidView(UserPassesTestMixin, TemplateView):

    template_name = 'users/logistic/auction/view_bid.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'bid'
    model = Bid

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user=self.request.user)

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_logistic or self.request.user.is_superuser)
