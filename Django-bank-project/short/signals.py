from django.contrib.auth import user_logged_in
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    print('User just logged in....')

# @receiver(user_logged_in)
# def post_login(sender, users, request, stuff=None, your=None, **kwargs):

