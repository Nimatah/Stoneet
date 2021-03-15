from django.db import models
from persiantools.jdatetime import JalaliDate

from apps.core.models import TimestampedModel
from apps.users.models import User
from apps.products.models import Attribute


class OrderQuerySet(models.QuerySet):

    def accepted(self):
        return self.filter(state=Order.STATE_ACCEPTED)

    def rejected(self):
        return self.filter(state=Order.STATE_PENDING_SELLER)

    def pending(self):
        return self.filter(state=Order.STATE_PENDING_SELLER)


class OrderManager(models.Manager):

    def get_queryset(self) -> 'OrderQuerySet':
        return OrderQuerySet(model=self.model, using=self.db)

    def get_by_seller(self, user: User) -> 'OrderQuerySet':
        return self.filter(product__user=user)

    def get_by_buyer(self, user: User) -> 'OrderQuerySet':
        return self.filter(buyer=user)


class LogisticOrderQuerySet(models.QuerySet):

    pass


class LogisticOrderManager(models.Manager):

    def get_queryset(self) -> 'LogisticOrderQuerySet':
        return LogisticOrderQuerySet(model=self.model, using=self.db)


class Order(TimestampedModel):

    STATE_SUBMITTED = 'submitted'
    STATE_PENDING_SELLER = 'pending_seller'
    STATE_PENDING_LOGISTIC = 'pending_logistic'
    STATE_PENDING_BUYER_LOGISTIC_PRICE = 'pending_buyer_logistic_price'
    STATE_PENDING_CONTRACT = 'pending_contract'
    STATE_PENDING_FINANCE_DOCUMENTS = 'pending_finance_documents'
    STATE_ACCEPTED = 'STATE_ACCEPTED'

    _STATE_CHOICES = (
        (STATE_SUBMITTED, 'ثبت سفارش',),
        (STATE_PENDING_SELLER, 'تایید فروشنده',),
        (STATE_PENDING_LOGISTIC, 'رد شده',),
        (STATE_PENDING_BUYER_LOGISTIC_PRICE, 'رد شده',),
        (STATE_PENDING_CONTRACT, 'رد شده',),
        (STATE_PENDING_FINANCE_DOCUMENTS, 'رد شده',),
        (STATE_ACCEPTED, 'رد شده',),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    buyer = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    commission = models.FloatField(null=True, blank=True)
    destination = models.ForeignKey('users.Address', on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    state = models.CharField(max_length=255, choices=_STATE_CHOICES, default=STATE_SUBMITTED)
    price = models.BigIntegerField()
    weight = models.IntegerField(null=True, blank=True)
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    monthly_load = models.IntegerField(default=0, null=True, blank=True)

    objects = OrderManager()

    def __str__(self):
        return f'{self.product} -> {self.buyer}'

    def get_persian_timestamp(self):
        return JalaliDate.to_jalali(self.timestamp)


class LogisticOrder(models.Model):

    STATE_PENDING = 'pending'
    STATE_ACCEPTED = 'accepted'
    STATE_REJECTED = 'rejected'

    _STATE_CHOICES = (
        (STATE_PENDING, 'در انتظار تایید',),
        (STATE_ACCEPTED, 'تایید شده',),
        (STATE_REJECTED, 'رد شده',),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    state = models.CharField(max_length=255, choices=_STATE_CHOICES)
    price = models.BigIntegerField()

    objects = LogisticOrderManager()

    def __str__(self):
        return f'Logistic Order: {self.order}'
