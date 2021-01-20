from django.views.generic import TemplateView


class BuyerProfileView(TemplateView):

    template_name = 'users/buyer/profile.html'
