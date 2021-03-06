from django.contrib.auth.views import LoginView as BaseLoginView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.users.forms import UserLoginForm


class LoginView(BaseLoginView):
    form_class = UserLoginForm
    template_name = 'users/auth/login.html'

    def get_redirect_url(self):
        return reverse_lazy('users:redirect')

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('users:redirect'))

    def form_invalid(self, form):
        return redirect(reverse_lazy('home:index') + '?login=fail')


class LoginRedirectView(UserPassesTestMixin, View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(f'{reverse_lazy("home:index")}users/panel/{self.request.user.use_type}-dashboard/')

    def test_func(self):
        return self.request.user.is_authenticated
