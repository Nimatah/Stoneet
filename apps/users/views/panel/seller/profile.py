from django.views.generic import TemplateView


class SellerProfileView(TemplateView):

    template_name = 'users/seller/profile.html'
