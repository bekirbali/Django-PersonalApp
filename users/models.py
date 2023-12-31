from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='images', default='avatar.png')
    about = models.TextField(null=True, blank=True)
    user =  models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username