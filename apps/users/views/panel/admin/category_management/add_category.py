from django.views.generic import FormView
from django.urls import reverse_lazy

from apps.products.forms.category import CategoryAddForm
from apps.products.models import Category


class AddCategoryView(FormView):
    template_name = 'users/admin/category_management/add_category.html'
    success_url = reverse_lazy('users:admin_list_category')
    form_class = CategoryAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['root_categories'] = Category.objects.get_root()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

