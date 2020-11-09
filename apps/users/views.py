from django.views.generic import FormView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView

from apps.users.forms import UserLoginForm, UserRegisterForm


class LoginView(BaseLoginView):

    form_class = UserLoginForm
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):

    pass


class RegisterView(FormView):

    form_class = UserRegisterForm
    template_name = 'users/register.html'
