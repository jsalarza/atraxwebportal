from django.db.models.deletion import ProtectedError, PROTECT
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Division(models.Model):
    division_description = models.CharField(max_length=200)

    def __str__(self):
        return self.division_description


class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district_description = models.CharField(max_length=200)

    def __str__(self):
        return self.district_description


class School(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_description = models.CharField(max_length=200)

    def __str__(self):
        return self.school_description


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=PROTECT, null=True)
    avatar_url = models.CharField(max_length=250, null=True, blank=True)
    termsconditions = models.BooleanField(null=False, blank=False, default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
