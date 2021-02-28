from django.views.generic import TemplateView


class AddCategoryView(TemplateView):
    template_name = 'users/admin/category_management/add_category.html'

