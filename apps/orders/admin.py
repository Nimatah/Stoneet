from django.contrib import admin

from apps.orders.models import Order, LogisticOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('timestamp', 'product', 'buyer', 'commission', 'destination',
                    'state', 'price', 'weight', 'payment_type', 'monthly_load')


@admin.register(LogisticOrder)
class AdminLogisticOrder(admin.ModelAdmin):

    pass
