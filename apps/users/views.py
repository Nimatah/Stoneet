from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import login
from django.http.response import HttpResponseRedirect

from apps.users.forms import UserLoginForm, UserRegisterForm


class LoginView(BaseLoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'


class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("home:index")

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('home:index'))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
