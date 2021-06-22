from django.views.generic import TemplateView

from apps.locations.models import Region


class SellerProfileView(TemplateView):

    template_name = 'users/seller/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context
