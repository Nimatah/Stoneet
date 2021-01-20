from django.views.generic import TemplateView


class ProfileView(TemplateView):

    template_name = 'users/seller/profile.html'
