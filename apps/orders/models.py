from django.db import models
from persiantools.jdatetime import JalaliDate

from apps.core.models import TimestampedModel, BaseMedia
from apps.core.utils import get_file_path
from apps.users.models import User
from apps.products.models import Attribute


def get_order_file_path(instance, filename):
    return get_file_path('orders/%Y/%m', filename)


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
        (STATE_SUBMITTED, 'ثبت سفارش',),
        (STATE_ADMIN, 'تایید سایت'),
        (STATE_SELLER, 'تایید فروشنده',),
        (STATE_LOGISTIC, 'تایید حمل و نقل',),
        (STATE_BUYER_LOGISTIC_PRICE, 'تایید قیمت حمل و نقل توسط خریدار',),
        (STATE_CONTRACT, 'تایید قرارداد',),
        (STATE_FINANCE_DOCUMENTS, 'تایید مدارک مالی',),
        (STATE_ACCEPTED, 'تایید نهایی',),
        (STATE_FINISHED, 'انجام شده',),
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

    objects = OrderManager()

    def __str__(self):
        return f'{self.product} -> {self.buyer}'

    def get_persian_timestamp(self):
        return JalaliDate.to_jalali(self.timestamp)

    def state_lt(self, state):
        return self.STATE_ORDER_MAP[self.state] < self.STATE_ORDER_MAP[state]

    def get_monthly_weight(self):
        return f'{(self.weight / self.monthly_load):.2f}'


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


class OrderMedia(BaseMedia):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='media')
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=get_order_file_path)


class LogisticOrderMedia(BaseMedia):

    order = models.ForeignKey(LogisticOrder, on_delete=models.CASCADE, related_name='media')
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=get_order_file_path)

