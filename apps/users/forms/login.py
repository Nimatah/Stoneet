from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):

    def clean_username(self):
        username = self.cleaned_data['username'].lower().strip()
        return username
