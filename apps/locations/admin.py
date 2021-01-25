from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from apps.locations.models import Region


@admin.register(Region)
class RegionAdmin(MPTTModelAdmin):

    list_display = ('title', 'parent',)
    search_fields = ('title', 'parent__title',)
    mptt_level_indent = 20
