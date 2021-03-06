from django.db import models
from persiantools.jdatetime import JalaliDate

from apps.core.models import TimestampedModel, BaseMedia
from apps.core.utils import get_file_path
from apps.users.models import User
from apps.products.models import Attribute


def get_order_file_path(instance, filename):
    return get_file_path('orders', filename)


class OrderQuerySet(models.QuerySet):

    def submitted(self):
        return self.filter(state=Order.STATE_SUBMITTED)

    def pending_seller(self):
        return self.filter(state=Order.STATE_SELLER)

    def pending_logistic(self):
        return self.filter(state=Order.STATE_LOGISTIC)

    def pending_buyer_logistic_price(self):
        return self.filter(state=Order.STATE_BUYER_LOGISTIC_PRICE)

    def pending_contract(self):
        return self.filter(state=Order.STATE_CONTRACT)

    def pending_finance_documents(self):
        return self.filter(state=Order.STATE_FINANCE_DOCUMENTS)

    def accepted(self):
        return self.filter(state=Order.STATE_ACCEPTED)

    def finished(self):
        return self.filter(state=Order.STATE_FINISHED)


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


class LogisticDrive(TimestampedModel):

    pass


class Order(TimestampedModel):

    STATE_SUBMITTED = 'submitted'
    STATE_ADMIN = 'pending_admin'
    STATE_SELLER = 'pending_seller'
    STATE_LOGISTIC = 'pending_logistic'
    STATE_BUYER_LOGISTIC_PRICE = 'pending_buyer_logistic_price'
    STATE_CONTRACT = 'pending_contract'
    STATE_FINANCE_DOCUMENTS = 'pending_finance_documents'
    STATE_ACCEPTED = 'accepted'
    STATE_FINISHED = 'finished'

    STATE_CHOICES = (
        (STATE_SUBMITTED, '?????? ??????????',),
        (STATE_ADMIN, '?????????? ????????'),
        (STATE_SELLER, '?????????? ??????????????',),
        (STATE_LOGISTIC, '?????????? ?????? ?? ??????',),
        (STATE_BUYER_LOGISTIC_PRICE, '?????????? ???????? ?????? ?? ?????? ???????? ????????????',),
        (STATE_CONTRACT, '?????????? ??????????????',),
        (STATE_FINANCE_DOCUMENTS, '?????????? ?????????? ????????',),
        (STATE_ACCEPTED, '?????????? ??????????',),
        (STATE_FINISHED, '?????????? ??????',),
    )

    STATE_ORDER_MAP = {
        STATE_SUBMITTED: 0,
        STATE_ADMIN: 1,
        STATE_SELLER: 2,
        STATE_LOGISTIC: 3,
        STATE_BUYER_LOGISTIC_PRICE: 4,
        STATE_CONTRACT: 5,
        STATE_FINANCE_DOCUMENTS: 6,
        STATE_ACCEPTED: 7,
        STATE_FINISHED: 8,
    }

    WEIGHT_TON = 'ton'
    WEIGHT_KILO = 'kilo'

    WEIGHT_CHOICES = (
        (WEIGHT_TON, '????',),
        (WEIGHT_KILO, '??????????????',),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    buyer = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    logistic_order = models.ForeignKey('LogisticOrder', on_delete=models.CASCADE, related_name='product_orders', null=True, blank=True)
    commission = models.FloatField(null=True, blank=True)
    destination = models.ForeignKey('users.Address', on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    state = models.CharField(max_length=255, choices=STATE_CHOICES, default=STATE_SUBMITTED)
    price = models.BigIntegerField()
    weight = models.IntegerField(null=True, blank=True)
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    monthly_load = models.IntegerField(default=1, null=True, blank=True)
    is_rejected = models.BooleanField(default=False)
    reject_reason = models.TextField(blank=True)

    objects = OrderManager()

    def __str__(self):
        return f'{self.product} -> {self.buyer}'

    def get_persian_timestamp(self):
        return JalaliDate.to_jalali(self.timestamp)

    def state_lt(self, state):
        return self.STATE_ORDER_MAP[self.state] < self.STATE_ORDER_MAP[state]

    def get_monthly_weight(self):
        return f'{(self.weight / self.monthly_load):.2f}'

    def get_contract(self):
        return self.media.filter(title='contract').first()

    def get_signed_contract_pages(self):
        return self.media.filter(title='signed_contract')

    def get_finance_documents(self):
        return self.media.filter(title='finance')


class LogisticOrder(models.Model):

    STATE_PENDING = 'pending'
    STATE_ACCEPTED = 'accepted'
    STATE_CONTRACT = 'contract'
    STATE_FINANCE_DOCUMENTS = 'finance'
    STATE_REJECTED = 'rejected'

    STATE_CHOICES = (
        (STATE_PENDING, '???? ???????????? ??????????',),
        (STATE_ACCEPTED, '?????????? ??????',),
        (STATE_CONTRACT, '?????????? ??????????',),
        (STATE_FINANCE_DOCUMENTS, '?????????? ?????????? ????????',),
        (STATE_REJECTED, '???? ??????',),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    state = models.CharField(max_length=255, choices=STATE_CHOICES)
    price = models.BigIntegerField()
    source = models.ForeignKey('users.Mine', on_delete=models.CASCADE, null=True, blank=True)
    destination = models.ForeignKey('users.Address', on_delete=models.CASCADE, null=True, blank=True)
    monthly_load_count = models.IntegerField(default=1)
    weight = models.BigIntegerField(default=0)

    objects = LogisticOrderManager()

    def __str__(self):
        return f'Logistic Order: {self.order}'

    def get_monthly_weight(self):
        try:
            return f'{self.weight / self.monthly_load_count:.2f}'
        except ZeroDivisionError:
            return self.weight

    def get_monthly_price(self):
        try:
            return f'{self.price / self.monthly_load_count:.2f}'
        except ZeroDivisionError:
            return self.price


class OrderMedia(BaseMedia):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='media')
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=get_order_file_path)


class LogisticOrderMedia(BaseMedia):

    order = models.ForeignKey(LogisticOrder, on_delete=models.CASCADE, related_name='media')
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=get_order_file_path)


class SampleOrder(TimestampedModel):

    STATE_PENDING = 'pending'
    STATE_ACCEPTED = 'accepted'
    STATE_SENT = 'sent'
    STATE_RECEIVED = 'received'
    STATE_REJECTED = 'rejected'

    STATE_CHOICES = (
        (STATE_PENDING, '???? ???????????? ??????????'),
        (STATE_ACCEPTED, '?????????? ??????'),
        (STATE_SENT, '?????????? ??????'),
        (STATE_RECEIVED, '???????????? ??????'),
        (STATE_REJECTED, '???? ??????'),
    )

    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='samples')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='samples')
    state = models.CharField(max_length=255, choices=STATE_CHOICES)

    def get_persian_timestamp(self):
        return JalaliDate.to_jalali(self.created_at)
