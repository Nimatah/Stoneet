from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class LogisticProfileView(UserPassesTestMixin, TemplateView):

    template_name = 'users/logistic/profile.html'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_logistic or self.request.user.is_superuser)
