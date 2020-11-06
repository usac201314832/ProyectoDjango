"""
    Modelo Proxy para usuarios de nuestro sistema
"""
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True) 
    last = models.CharField(max_length=50, blank=True)
    age = models.CharField(max_length=4, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    userImage = models.ImageField(
        upload_to = "users/pictures",
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username