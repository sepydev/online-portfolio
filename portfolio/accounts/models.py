from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(default='1.jpg')

    class Meta:
        verbose_name = 'User'


class Profile(models.Model):
    user = models.OneToOneField('User', models.CASCADE)
    job_title = models.CharField(max_length=155, verbose_name="Job title", blank=True, default='')

