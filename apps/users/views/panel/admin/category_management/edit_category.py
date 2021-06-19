from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect

from apps.products.forms.category import CategoryEditForm
from apps.products.models import Category


def edit_category(request, pk):
    instance = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        form = CategoryEditForm()
        return render(request, 'users/admin/category_management/edit_category.html',
                      context={
                          'form': form,
                          'category': instance,
                          'root_categories': Category.objects.get_root(),
                      })
    else:
        form = CategoryEditForm(request.POST)
        form.instance = instance
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('users:admin_list_category'))
        raise Exception
