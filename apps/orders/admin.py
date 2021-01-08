from django.contrib import admin

from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('timestamp', 'product', 'buyer', 'price',)

