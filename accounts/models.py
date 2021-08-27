from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


# Create your models here.


class User(AbstractUser):
    country = models.CharField(max_length=25, blank=True, unique=True, null=True)


