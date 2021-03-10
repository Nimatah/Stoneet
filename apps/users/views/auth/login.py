from django.contrib.auth.views import LoginView as BaseLoginView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render

from apps.users.forms import UserLoginForm


class LoginView(BaseLoginView):
    form_class = UserLoginForm
    template_name = 'users/auth/login.html'

    def get_redirect_url(self):
        return reverse_lazy('users:redirect')

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('users:redirect'))

    def form_invalid(self, form):
        return render(
            self.request,
            'home/home.html',
            context={
                'form': form,
                'error_message': 'نام کاربری یا رمز عبور اشتباه است'
            }
        )


class LoginRedirectView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(f'{reverse_lazy("home:index")}users/panel/{self.request.user.use_type}-dashboard/')
