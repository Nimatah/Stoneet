from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import login
from django.http.response import HttpResponseRedirect

from apps.users.forms import UserLoginForm, UserRegisterForm


class LoginView(BaseLoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('home:index'))
        return super().get(request, *args, **kwargs)


class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("home:index")

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('home:index'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserPanelView(TemplateView):

    template_name = 'base_admin.html'


class AddProductView(TemplateView):

    template_name = 'users/add_product.html'
