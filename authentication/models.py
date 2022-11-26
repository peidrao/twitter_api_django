from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Profile(AbstractUser):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    web_site = models.URLField(blank=True, null=True)
    bio = models.CharField(max_length=160, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    picture = models.ImageField(upload_to="profile/pic", null=True)
    banner = models.ImageField(upload_to="profile/banner", null=True)

    birth_date = models.DateField(null=True)
    is_professional = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name
