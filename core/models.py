"""
Database models
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self,email,password=None, **extra_fields):   #**extra_field --Keyword argument that can be passed to user model
        """Create, save and return a new user"""
        if not email:
            raise ValueError('User must have email address')

        user = self.model(email = self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email,password):
        """create and return new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    #Field that we wanna use for authentication


'''
-->Explaination for self.model

we're calling self. model.
And what this is, is because our manager is associated to a model, we need a way of being able to
access the model that we're associated with.
So the way that you do that with a Django model manager is you can just call self . model and it will
be the same as defining a new user object out of our user clause because that is the manager, the user
is going to be assigned to it.
So essentially we're creating a new user model.
We're passing in the email address that is being provided and then we're passing in any extra fields
that were provided when they're called create user.


-->set_password

It will take the password that's provided in the create user method.
And it will encrypt it through a hashing mechanism. That means it has a one way encryption that can't be reversed.

-->self._db
this is just to support adding multiple databases if you choose to add multiple databases to your project.

-->objects = UserManager()

assign this user manager to our custom

user clause and we do that by typing objects equals user manager and we'll add the bracket set.

So it creates an instance of the manager.

And this is how you assign a user manager in Django.
'''
