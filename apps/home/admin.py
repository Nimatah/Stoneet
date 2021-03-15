from django.contrib import admin

from .models import StaticContent


@admin.register(StaticContent)
class StaticContentAdmin(admin.ModelAdmin):

    def has_add_permission(self, *args, **kwargs):
        return not StaticContent.objects.exists()

