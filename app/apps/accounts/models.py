from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
  def create_user(self, email, password, **extra_fields):
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()

    profile = UserProfile.objects.create(user=user)
    profile.save()

    return user

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')
    return self.create_user(email, password, **extra_fields)

class UserAccount(AbstractUser):
  objects = UserManager()
  
  def __str__(self):
    return self.email

class UserProfile(models.Model):
  user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)

  # Profile fields
  biography = models.TextField(null=True, blank=True)

  # Privacy settings
  show_email = models.BooleanField(null=True, default=False)
  show_fullname = models.BooleanField(null=True, default=False)
  show_biography = models.BooleanField(null=True, default=True)
  show_my_creations = models.BooleanField(null=True, default=True)
  show_my_organisations = models.BooleanField(null=True, default=True)

  def __str__(self):
    return f'Profile of User: {self.user.username}'
