from django.db import models


class Media(models.Model):
    TYPE_CHOICES = (
        ("image", "Image",),
        ("document", "Document",),
    )

    PURPOSE_CHOICES = (
        ("registration", "Registration",),
        ("order", "Order",),
    )

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    file = models.FileField()

    def __str__(self):
        return f"{self.user.name} {self.type}"
