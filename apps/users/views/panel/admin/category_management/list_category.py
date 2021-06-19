from django.views.generic import ListView

from apps.products.models import Category


class ListCategoryView(ListView):
    template_name = 'users/admin/category_management/list_category.html'
    model = Category
    context_object_name = 'categories'
