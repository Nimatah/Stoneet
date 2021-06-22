import base64

from django.db import models


class BaseProfileManager(models.Manager):
    pass


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

    NAME_CONTRACT = 'contract'

    type = models.CharField(max_length=20, choices=_TYPE_CHOICES)
    file = models.FileField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.type}'

    def to_base64(self):
        position = self.file.tell()
        stream = self.file.read()
        self.file.seek(position)
        return base64.b64encode(stream).decode('utf-8')
