from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """" Helps django work with custom user model"""

    def create_user(self, email, name, password=None):
        """" creates a new user object"""
        if not email:
            raise ValueError('Users must have an email')
        email = self.normalize_email(email)
        # convert email to lowercase
        user = self.model(email=email, name=name)
        # creates user object
        user.set_password(password)
        # saves password
        user.save(using=self._db)
        # saves user
        return user

    def create_superuser(self, email, name, password):
        """ creates superuser /admin with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Respresent User Profile in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    """ helper functions"""

    def get_full_names(self):
        """ used to get a users full name"""
        return self.name

    def get_short_name(self):
        """ Used to get a users short name."""
        return self.name

    def __str__(self):
        """ converts an object to string"""
        return self.email

class ProfileFeedItem(models.Model):
    """ profile status update"""
    user_profile=models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ return model as a string"""
        return self.status_text