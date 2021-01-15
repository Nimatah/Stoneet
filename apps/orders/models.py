from django.db import models

from apps.core.models import TimestampedModel


class OrderManager(models.Manager):
    pass


class LogisticOrderManager(models.Manager):
    pass


class Order(TimestampedModel):

    STATE_PENDING = 'pending'
    STATE_ACCEPTED = 'accepted'
    STATE_REJECTED = 'rejected'

    _STATE_CHOICES = (
        (STATE_PENDING, 'Pending',),
        (STATE_ACCEPTED, "Accepted",),
        (STATE_REJECTED, 'Rejected',),
    )

    PAYMENT_CASH = 'cash'
    PAYMENT_INSTALLMENT = 'installment'

    _PAYMENT_CHOICES = (
        (PAYMENT_CASH, 'Cash',),
        (PAYMENT_INSTALLMENT, 'Installment',),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    buyer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    state = models.CharField(max_length=255, choices=_STATE_CHOICES, default=STATE_PENDING)
    price = models.BigIntegerField()
    payment_type = models.CharField(max_length=255, choices=_PAYMENT_CHOICES, default=PAYMENT_CASH)
    installment_months = models.IntegerField(default=0)

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
