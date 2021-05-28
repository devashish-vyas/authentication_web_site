from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) # if the user is deleted cascade means that profile will also be deleted
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self): #tells how to print profile
        return f'{self.user.username}Profile'

