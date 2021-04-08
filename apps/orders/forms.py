from django import forms
from django.db import transaction

from apps.products.models import Product, Attribute
from apps.orders.models import Order, OrderMedia

from apps.users.models import Address


class CreateOrderForm(forms.ModelForm):

    product = forms.IntegerField()
    buyer = forms.IntegerField(required=False)
    commission = forms.FloatField(required=False)
    destination = forms.IntegerField()
    price = forms.IntegerField(required=False)
    weight = forms.IntegerField()
    payment_type = forms.CharField()
    monthly_load = forms.IntegerField()

    class Meta:
        model = Order
        fields = ('product', 'buyer', 'commission', 'destination', 'price',
                  'weight', 'payment_type', 'monthly_load')
        exclude = ('buyer', 'commission', 'price')

    def clean_product(self):
        try:
            return Product.objects.get(pk=self.cleaned_data['product'])
        except Product.DoesNotExist:
            raise forms.ValidationError('محصول پیدا نشد')

    def clean_destination(self):
        try:
            return Address.objects.get(pk=self.cleaned_data['destination'])
        except Address.DoesNotExist:
            raise forms.ValidationError('آدرس پیدا نشد')

    def clean_payment_type(self):
        if self.cleaned_data['payment_type'] not in (Attribute.PAYMENT_MAP.keys()):
            raise forms.ValidationError('نوع پرداخت اشتباه است')
        return self.cleaned_data['payment_type']

    def save(self, commit=True):
        order = Order()
        order.product = self.cleaned_data['product']
        order.buyer = self.buyer
        order.commission = self.cleaned_data['product'].get_commission()
        order.destination = self.cleaned_data['destination']
        order.state = Order.STATE_SUBMITTED
        order.weight = self.cleaned_data['weight']
        order.price = self.cleaned_data['product'].get_price().value * self.cleaned_data['weight']
        order.payment_type = self.cleaned_data['payment_type']
        order.monthly_load = self.cleaned_data['monthly_load']

        if commit:
            order.save()
        return order


class AdminApproveOrderForm(forms.Form):

    id = forms.IntegerField()
    state = forms.CharField()
    contract = forms.ImageField()

    def clean_id(self):
        if not Order.objects.filter(pk=self.cleaned_data['id']).exists():
            raise forms.ValidationError('کد سفارش پیدا نشد')
        return self.cleaned_data['id']

    def clean_state(self):
        if self.cleaned_data['state'] not in dict(Order.STATE_CHOICES).keys():
            raise forms.ValidationError('وضعیت اشتباه است')
        return self.cleaned_data['state']

    def save(self, commit=True):
        order = Order.objects.get(pk=self.cleaned_data['id'])
        order.state = self.cleaned_data['state']
        order_media = OrderMedia(
            order=order,
            title='contract',
            file=self.cleaned_data['contract'],
            type=OrderMedia.TYPE_IMAGE,
        )
        if commit:
            with transaction.atomic():
                order.save()
                order_media.save()
        return order
