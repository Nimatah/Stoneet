from django.views.generic import FormView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login

from apps.users.forms import UserRegisterForm


class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'users/auth/register.html'
    success_url = reverse_lazy("home:index")

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('home:index'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
