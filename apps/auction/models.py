from django.db import models


class Auction(models.Model):

    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)


class Bid(models.Model):

    auction = models.ForeignKey('Auction', on_delete=models.CASCADE, related_name='auction')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

