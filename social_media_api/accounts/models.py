from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True )
    followers = models.ManyToManyField("self",symmetrical=False, related_name="followed_by", blank=True)
    groups = models.ManyToManyField("auth.Group", blank=True, related_name="customuser_set")
    user_permissions = models.ManyToManyField("auth.permission", blank=True, related_name="customuser_set")