from django.contrib.auth.views import LoginView as BaseLoginView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View

from apps.users.forms import UserLoginForm


class LoginView(BaseLoginView):
    form_class = UserLoginForm
    template_name = 'users/auth/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('users:redirect'))
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self):
        return reverse_lazy('users:redirect')


class LoginRedirectView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(f'{reverse("home:index")}users/panel/{self.request.user.use_type}-dashboard/')
