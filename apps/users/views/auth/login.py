from django.contrib.auth.views import LoginView as BaseLoginView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

from apps.users.forms import UserLoginForm


class LoginView(BaseLoginView):
    form_class = UserLoginForm
    template_name = 'users/auth/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('home:index'))
        return super().get(request, *args, **kwargs)
