from django.views.generic import TemplateView


class UserDashboardView(TemplateView):

    template_name = 'users/seller/dashboard.html'
