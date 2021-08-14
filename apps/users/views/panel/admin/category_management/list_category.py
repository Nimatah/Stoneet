from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from apps.products.models import Category


class ListCategoryView(UserPassesTestMixin, ListView):
    template_name = 'users/admin/category_management/list_category.html'
    model = Category
    context_object_name = 'categories'

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin or self.request.user.is_superuser)
