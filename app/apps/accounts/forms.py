from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields
from .models import UserAccount

class UserAccountCreationForm(UserCreationForm):
  class Meta:
    model = UserAccount
    fields = ('username', 'email')

class UserAccountChangeForm(UserChangeForm):
  class Meta:
    model = UserAccount
    fields = ('username', 'email')
