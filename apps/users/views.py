from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import login
from django.http.response import HttpResponseRedirect

from apps.users.forms import UserLoginForm, UserRegisterForm
from apps.products.forms import AddProductForm
from apps.products.models import Category, Attribute


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


class UserDashboardView(TemplateView):

    template_name = 'users/dashboard.html'


class AddProductView(FormView):
    form_class = AddProductForm
    template_name = 'users/add_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [c.to_dict_hierarchy() for c in Category.objects.get_root().prefetch_related('children')]
        context['attributes_field'] = Attribute.objects.filter(value_type__in=['int', 'dropdown', 'string', 'float'])
        context['attributes_image'] = Attribute.objects.filter(value_type='image')
        context['attributes_bool'] = Attribute.objects.filter(value_type='bool')
        return context

    def form_valid(self, form):
        form.user = self.request.user
        form.save()
        return super().form_valid(form)


class ListProductView(TemplateView):

    template_name = 'users/list_product.html'


class EditProductView(TemplateView):

    template_name = 'users/edit_product.html'
