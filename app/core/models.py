from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self, email, password):
        """Create, save and return a new user"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_freelancer = models.BooleanField(default=False)

    objects = UserManager()
    # assign the custom manager to the user model
    # this allows creating and managing users using custom
    # methods like create_user

    USERNAME_FIELD = 'email'
    # specifies the field to be used as the unique identifier for authentication
