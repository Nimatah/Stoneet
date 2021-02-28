from django.views.generic import TemplateView


class ListCategoryView(TemplateView):
    template_name = 'users/admin/category_management/list_category.html'
