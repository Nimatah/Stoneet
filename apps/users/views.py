from django.contrib.auth.views import LoginView as BaseLoginView

from apps.users.forms import UserLoginForm


class LoginView(BaseLoginView):

    form_class = UserLoginForm
    template_name = 'users/login.html'
