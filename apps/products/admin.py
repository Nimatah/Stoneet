from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from apps.products.models import Attribute, Category, Product, ProductAttribute, ProductMedia


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('title', 'value_type', 'options', 'unit')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title', 'parent', 'is_active', 'commission',)
    search_fields = ('title',)
    filter_horizontal = ('attributes',)
    mptt_level_indent = 20


class ProductAttributeAdminInline(admin.TabularInline):
    model = ProductAttribute


class ProductMediaAdminInline(admin.TabularInline):
    model = ProductMedia


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category',)
    search_fields = ('title',)

    inlines = (ProductAttributeAdminInline, ProductMediaAdminInline)

