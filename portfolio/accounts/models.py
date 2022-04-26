from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    image = models.ImageField(default='1.jpg')

    class Meta:
        verbose_name = 'User'


@receiver(post_save, sender=User)
def insert_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField('User', models.CASCADE)
    job_title = models.CharField(max_length=155, verbose_name="Job title", blank=True, default='')

    def __str__(self):
        return self.user.username
