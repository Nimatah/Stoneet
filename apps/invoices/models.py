from django.db import models


class Invoice(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)


class Receipt(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
