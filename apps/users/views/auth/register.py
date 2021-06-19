from django.views.generic import FormView, TemplateView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login

from apps.locations.models import Region
from apps.users.forms import (
    SellerRegisterForm,
    BuyerRegisterForm,
    LogisticRegisterForm
)


class SellerRegisterView(FormView):
    template_name = 'users/auth/register/register_seller.html'
    form_class = SellerRegisterForm
    success_url = reverse_lazy("users:redirect")

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('users:redirect'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context


class BuyerRegisterView(FormView):
    template_name = 'users/auth/register/register_buyer.html'
    form_class = BuyerRegisterForm
    success_url = reverse_lazy('users:redirect')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('users:redirect'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context


class LogisticRegisterView(FormView):

    template_name = 'users/auth/register/register_logistic.html'
    form_class = LogisticRegisterForm
    success_url = reverse_lazy('users:redirect')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('users:redirect'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.to_context()
        return context
