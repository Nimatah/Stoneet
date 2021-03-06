from django.views.generic import TemplateView

from apps.locations.models import Region


class BuyerProfileView(TemplateView):

    template_name = 'users/buyer/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = [r.to_dict_hierarchy() for r in Region.objects.get_root().prefetch_related('children')]
        return context
