from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) # if the user is deleted cascade means that profile will also be deleted
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self): #tells how to print profile
        return f'{self.user.username}Profile'

    def save(self): #overriding save method of a model
        super().save()#run the save method of super class

        img=Image.open(self.image.path) #to resize a big image to 300px 
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


