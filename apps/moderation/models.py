from django.db import models

from apps.core.models import TimestampedModel
from apps.users.models import User


class Ticket(TimestampedModel):

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    description = models.TextField()


class ProfileChangeRequest(TimestampedModel):

    STATE_PENDING = 'pending'
    STATE_RESOLVED = 'resolved'
    STATE_REJECTED = 'rejected'
    STATE_CHOICES = (
        (STATE_PENDING, 'در حال بررسی'),
        (STATE_RESOLVED, 'انجام شده'),
        (STATE_REJECTED, 'رد شده'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=255, choices=STATE_CHOICES)
    description = models.TextField()
