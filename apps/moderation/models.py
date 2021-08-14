from django.db import models

from apps.core.models import TimestampedModel
from apps.users.models import User


class Ticket(TimestampedModel):

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    description = models.TextField()


class ProfileChangeRequest(TimestampedModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
