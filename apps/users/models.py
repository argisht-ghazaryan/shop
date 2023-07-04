from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    photo = models.ImageField(upload_to='profile_photo', blank=True)
    phone = PhoneNumberField(blank=True, help_text='Phone number')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile_model(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
