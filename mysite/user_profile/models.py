#from django.contrib.auth.models import AbstractUser
#from django.conf import settings
from django.db import models
from django.contrib.auth.models import User




class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   photo = models.ImageField(upload_to='user_profile/img/%Y/%m/%d/', blank=True, default='')
   is_admin = models.BooleanField(default=False)
   is_manager = models.BooleanField(default=False)


   def __str__(self):
       return f"{self.id} - {self.user.username}"   


class SocialMedia(models.Model):
   url = models.URLField(null=False, blank=False)
   name = models.CharField(max_length=50, null=False, blank=False)
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)





"""
class UserProfile(AbstractUser):
photo = models.ImageField(upload_to='user/img/%Y/%m/%d/', blank=True, default=None)
is_admin = models.BooleanField(default=False)
is_manager = models.BooleanField(default=False)
class Meta(AbstractUser.Meta):
   swappable = 'AUTH_USER_MODEL'


'''
Isso evita o conflito dos acessores reverso no django
já que estou herdando todos campos de AbstractUser
'''
UserProfile._meta.get_field('groups').related_name = 'user_profile_groups'
UserProfile._meta.get_field('user_permissions').related_name = 'user_profile_user_permissions'
"""
