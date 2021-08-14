from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.users.models import User
from apps.users.filters import AdminUserFilter


class ListAdminView(UserPassesTestMixin, ListView):
    template_name = 'users/admin/user_management/list_user/list_admin.html'
    queryset = User.objects.filter(use_type=User.TYPE_ADMIN)
    context_object_name = 'users'
    page_kwarg = 'p'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class ListSellerView(UserPassesTestMixin, ListView):
    template_name = 'users/admin/user_management/list_user/list_seller.html'
    context_object_name = 'users'
    page_kwarg = 'p'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['states_choices'] = dict(User.STATE_CHOICES)
        return context

    def get_queryset(self):
        queryset = User.objects.filter(use_type=User.TYPE_SELLER)
        queryset = AdminUserFilter(self.request.GET, queryset=queryset).qs
        return queryset

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class ListBuyerView(UserPassesTestMixin, ListView):
    template_name = 'users/admin/user_management/list_user/list_buyer.html'
    queryset = User.objects.filter(use_type=User.TYPE_BUYER)
    context_object_name = 'users'
    page_kwarg = 'p'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['states_choices'] = dict(User.STATE_CHOICES)
        return context

    def get_queryset(self):
        queryset = User.objects.filter(use_type=User.TYPE_BUYER)
        queryset = AdminUserFilter(self.request.GET, queryset=queryset).qs
        return queryset

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)


class ListLogisticView(UserPassesTestMixin, ListView):
    template_name = 'users/admin/user_management/list_user/list_logistic.html'
    queryset = User.objects.filter(use_type=User.TYPE_LOGISTIC)
    context_object_name = 'users'
    page_kwarg = 'p'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['states_choices'] = dict(User.STATE_CHOICES)
        return context

    def get_queryset(self):
        queryset = User.objects.filter(use_type=User.TYPE_LOGISTIC)
        queryset = AdminUserFilter(self.request.GET, queryset=queryset).qs
        return queryset

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
