from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
    #used to create normal users
    def create_user(self, first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")

        user = self.model(
          email = self.normalize_email(email),
          username = username,
          first_name = first_name,
          last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    #used to create super users
    def create_superuser(self, first_name, last_name, username, email, password):
        superuser = self.create_user(
            email= self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        superuser.is_admin = True
        superuser.is_staff = True
        superuser.is_active = True
        superuser.is_superadmin = True
        superuser.save(using=self._db)
        return superuser


class Account(AbstractBaseUser):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(max_length=300,unique=True)
    phone_number = models.CharField(max_length=20)

    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','username']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True





# Create your models here.
