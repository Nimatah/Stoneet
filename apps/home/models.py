from django.db import models


class StaticContent(models.Model):

    terms = models.TextField(blank=True)
    terms_conditions = models.TextField(blank=True)
    terms_logistic = models.TextField(blank=True)
    privacy_policy = models.TextField(blank=True)
