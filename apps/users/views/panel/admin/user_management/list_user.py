from django.views.generic import ListView

from apps.users.models import User
from apps.users.filters import AdminUserFilter


class ListAdminView(ListView):
    template_name = 'users/admin/user_management/list_user/list_admin.html'
    queryset = User.objects.filter(use_type=User.TYPE_ADMIN)
    context_object_name = 'users'
    page_kwarg = 'p'
    paginate_by = 10


class ListSellerView(ListView):
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


class ListBuyerView(ListView):
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


class ListLogisticView(ListView):
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
