from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.locations.models import Region


class BuyerProfileView(UserPassesTestMixin, TemplateView):

    template_name = 'users/buyer/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_buyer or self.request.user.is_superuser)
