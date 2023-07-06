from django.db.models.signals import post_save
from django.dispatch import receiver
from pinpoint.settings.base import AUTH_USER_MODEL
from .models import Profile


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# if to customize something upon saving
@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    
    # further customization
    instance.profile.save()