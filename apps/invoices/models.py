from django.db import models

from apps.users.models import User


class InvoiceQuerySet(models.QuerySet):

    pass


class InvoiceManager(models.Manager):

    def get_queryset(self) -> 'InvoiceQuerySet':
        return InvoiceQuerySet(model=self.model, using=self.db)

    def get_by_user(self, user: User) -> 'InvoiceQuerySet':
        return self.filter(user=user)


class ReceiptQuerySet(models.QuerySet):

    pass


class ReceiptManager(models.Manager):

    def get_queryset(self) -> 'ReceiptQuerySet':
        return ReceiptQuerySet(model=self.model, using=self.db)

    def get_by_user(self, user: User) -> 'ReceiptQuerySet':
        return self.filter(user=user)


class Invoice(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)


class Receipt(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
