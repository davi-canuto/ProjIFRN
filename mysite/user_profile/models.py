#from django.contrib.auth.models import AbstractUser
#from django.conf import settings
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User




class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   photo = models.ImageField(upload_to='user_profile/img/%Y/%m/%d/', blank=True, default='')
   is_admin = models.BooleanField(default=False)
   is_manager = models.BooleanField(default=False)
   
   def __str__(self):
       return f"{self.id} - {self.user.username}"   

class TypeMedia(models.Model):
   icon = models.ImageField(upload_to='user_profile/type_media/', null=False)
   name = models.CharField(max_length=50, null=False, blank=False)


class SocialMedia(models.Model):
   url = models.URLField(null=False, blank=False)
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
   type_media = models.ForeignKey(TypeMedia, on_delete=models.SET_NULL, null=True)

