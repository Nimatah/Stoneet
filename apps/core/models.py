from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class BaseMedia(models.Model):
    TYPE_IMAGE = 'image'
    TYPE_DOCUMENT = 'document'

    _TYPE_CHOICES = (
        (TYPE_IMAGE, "Image",),
        (TYPE_DOCUMENT, "Document",),
    )

    type = models.CharField(max_length=20, choices=_TYPE_CHOICES)
    file = models.FileField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.type}'
