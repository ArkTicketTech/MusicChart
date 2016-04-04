# -*- coding: utf-8 -*-
# python
import json
# rest_framework
from rest_framework.authtoken.models import Token
# django
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        t = Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, username , password):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username , password):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username = username,
        )

        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=100,  unique=True, default="")
    # password = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
