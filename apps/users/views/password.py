from django.views.generic import TemplateView


class ResetPasswordView(TemplateView):
    template_name = 'users/auth/reset_password.html'


class PasswordConfirmationView(TemplateView):
    template_name = 'users/auth/password_confirmation.html'
