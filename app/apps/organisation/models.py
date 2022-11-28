from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Organisation(models.Model):
  id = models.AutoField(primary_key=True)

  # Organisation details
  created = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='organisation_owner')
  members = models.ManyToManyField(User, through='Membership')

  # Organisation profile
  name = models.CharField(max_length=250)
  biography = models.TextField(null=True, blank=True)
  website = models.URLField(max_length=1000, blank=True, null=True)
  email_contact = models.EmailField(null=True, blank=True)
  
  # Organisation privacy
  show_biography = models.BooleanField(null=True, default=True)
  show_contact = models.BooleanField(null=True, default=True)
  show_creations = models.BooleanField(null=True, default=True)
  show_members = models.BooleanField(null=True, default=False)

  class Meta:
    ordering = ('name', )

  def __str__(self):
    return f'Organisation: {self.name}'

class Membership(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
  
  # Join date
  joined = models.DateTimeField(auto_now_add=True)
  
  # Membership permissions
  able_to_modify = models.BooleanField(null=True, default=False)
  able_to_edit = models.BooleanField(null=True, default=False)
  able_to_create = models.BooleanField(null=True, default=False)
  able_to_delete = models.BooleanField(null=True, default=False)

  def __str__(self):
    return f'Membership<User:{self.user.username}, Organisation:{self.organisation.name}>'
