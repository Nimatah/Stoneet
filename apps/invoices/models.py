from django.db import models
from persiantools.jdatetime import JalaliDate

from apps.users.models import User


class InvoiceQuerySet(models.QuerySet):

    pass


class InvoiceManager(models.Manager):

    def get_queryset(self) -> 'InvoiceQuerySet':
        return InvoiceQuerySet(model=self.model, using=self.db)

    def get_by_user(self, user: User) -> 'InvoiceQuerySet':
        return self.filter(user=user)


class Invoice(models.Model):

    TYPE_SELLER = 'seller'
    TYPE_BUYER = 'buyer'
    TYPE_LOGISTIC = 'logistic'

    TYPE_CHOICES = (
        (TYPE_SELLER, 'فروشنده'),
        (TYPE_BUYER, 'خریدار',),
        (TYPE_LOGISTIC, 'باربری',),
    )

    STATE_PRE = 'پیش فاکتور'
    STATE_PAID = 'پرداخت شده'
    STATE_UNPAID = 'پرداخت نشده'

    STATE_CHOICES = (
        (STATE_PRE, 'پیش فاکتور',),
        (STATE_PAID, 'پرداخت شده',),
        (STATE_UNPAID, 'پرداخت نشده',),
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    guaranty = models.BigIntegerField(default=0)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, null=True)
    logistic_order = models.ForeignKey('orders.LogisticOrder', on_delete=models.CASCADE, null=True)
    auction = models.ForeignKey('auction.Auction', on_delete=models.CASCADE, null=True)
    timestamp = models.DateField(auto_now_add=True, null=True)
    publish_at = models.DateField(null=True)
    due_at = models.DateField(null=True)
    state = models.CharField(max_length=255, choices=STATE_CHOICES)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, null=True, blank=True)

    def get_persian_timestamp(self):
        if not self.timestamp:
            return ''
        return JalaliDate.to_jalali(self.timestamp)

    def get_persian_due_at(self):
        if not self.due_at:
            return ''
        return JalaliDate.to_jalali(self.due_at)

    def get_final_price(self):
        if self.logistic_order:
            return self.logistic_order.price + (self.logistic_order.price * (9 / 100))
        return self.order.price + (self.order.price * (9 / 100))

    def get_vat(self):
        if self.logistic_order:
            return self.logistic_order.price * (9 / 100)
        return self.order.price * (9 / 100)
