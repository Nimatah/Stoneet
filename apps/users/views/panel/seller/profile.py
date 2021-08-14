from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.locations.models import Region


class SellerProfileView(UserPassesTestMixin, TemplateView):

    template_name = 'users/seller/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_seller or self.request.user.is_superuser)
