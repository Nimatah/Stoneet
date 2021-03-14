from django.db import models

from apps.core.models import TimestampedModel
from apps.users.models import User
from apps.products.models import Attribute


class OrderQuerySet(models.QuerySet):

    def accepted(self):
        return self.filter(state=Order.STATE_ACCEPTED)

    def rejected(self):
        return self.filter(state=Order.STATE_REJECTED)

    def pending(self):
        return self.filter(state=Order.STATE_PENDING)


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

    STATE_PENDING = 'pending'
    STATE_ACCEPTED = 'accepted'
    STATE_REJECTED = 'rejected'

    _STATE_CHOICES = (
        (STATE_PENDING, 'Pending',),
        (STATE_ACCEPTED, "Accepted",),
        (STATE_REJECTED, 'Rejected',),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='orders')
    buyer = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='orders')
    commission = models.FloatField()
    destination = models.ForeignKey('users.Address', on_delete=models.CASCADE, related_name='orders')
    state = models.CharField(max_length=255, choices=_STATE_CHOICES, default=STATE_PENDING)
    price = models.BigIntegerField()
    weight = models.IntegerField()
    payment_type = models.CharField(max_length=255)
    monthly_load = models.IntegerField(default=0)

    objects = OrderManager()

    def __str__(self):
        return f'{self.product} -> {self.buyer}'


class LogisticOrder(models.Model):

    STATE_PENDING = 'pending'
    STATE_ACCEPTED = 'accepted'
    STATE_REJECTED = 'rejected'

    _STATE_CHOICES = (
        (STATE_PENDING, 'Pending',),
        (STATE_ACCEPTED, "Accepted",),
        (STATE_REJECTED, 'Rejected',),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    state = models.CharField(max_length=255, choices=_STATE_CHOICES)
    price = models.BigIntegerField()

    objects = LogisticOrderManager()

    def __str__(self):
        return f'Logistic Order: {self.order}'
