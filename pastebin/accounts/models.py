from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# You can add additional fields to the User model if needed
# Example: Add a profile picture field
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='', blank=True)
    username = models.CharField(max_length=255,default='')
    password = models.CharField(max_length = 255,default='')

    def __str__(self):
        return self.user.username
    
