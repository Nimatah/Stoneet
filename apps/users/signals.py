from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.users.models import User, Profile


# TODO: handle users without profile
@receiver(post_save, sender=User)
def initial_user_profile(sender: User, instance: User, created: bool, **kwargs):
    return
    if created:
        if not hasattr(instance, 'profile'):
            profile = Profile.objects.create(user=instance)
            instance.profile = profile
            instance.save()
