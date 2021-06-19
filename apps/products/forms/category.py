from django import forms

from apps.products.models import Category


class CategoryAddForm(forms.Form):

    title = forms.CharField(required=True)
    parent = forms.CharField(required=False)
    commission = forms.IntegerField(required=True)

    def clean_title(self):
        value = self.cleaned_data['title']
        return value.strip()

    def clean_parent(self):
        if self.cleaned_data['parent'] == '':
            return None
        return Category.objects.get(pk=self.cleaned_data['parent'])

    def save(self, *args, **kwargs):
        return Category.objects.create(
            title=self.cleaned_data['title'],
            parent=self.cleaned_data['parent'],
            commission=self.cleaned_data['commission'],
        )


class CategoryEditForm(forms.Form):

    title = forms.CharField(required=True)
    parent = forms.CharField(required=False)
    commission = forms.IntegerField(required=True)

    def clean_title(self):
        value = self.cleaned_data['title']
        return value.strip()

    def clean_parent(self):
        if self.cleaned_data['parent'] == '':
            return None
        return Category.objects.get(pk=self.cleaned_data['parent'])

    def save(self, *args, **kwargs):
        self.instance.title = self.cleaned_data['title']
        self.instance.parent = self.cleaned_data['parent']
        self.instance.commission = self.cleaned_data['commission']
        self.instance.save()
        return self.instance
