from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Respresent User Profile in the system """
    email=models.EmailField(max_length=255,unique)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    """ helper functions""""
    def get_full_names(self):
        """ used to get a users full name""""
        return self.name
    def get_short_name(self):
        """ Used to get a users short name.""""
        return self.name

    def __str__(self):
        """ converts an object to string""""
        return self.email
