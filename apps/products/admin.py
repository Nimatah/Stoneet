from django.contrib import admin

from apps.products.models import Attribute, Category, Product, ProductAttribute, Variant


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('title', 'value_type', 'options', 'unit')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'is_active', 'commission',)
    search_fields = ('title',)
    filter_horizontal = ('attributes',)


class ProductAttributeAdminInline(admin.TabularInline):
    model = ProductAttribute


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category',)
    search_fields = ('title',)


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ()

    inlines = (ProductAttributeAdminInline,)
