from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Brand(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=250, unique=True)
  description = models.TextField(blank=True, null=True)
  logo_path = models.CharField(max_length=250, null=True)
  website = models.URLField(max_length=1000, blank=True, null=True)
  owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name='brand_owner')
  site_title = models.CharField(max_length=50, blank=True, null=True)

  class Meta:
    ordering = ('name', )

  def __str__(self):
    return self.name

class Tag(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  
  created_by = models.ForeignKey(User,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name='tag_creator')
  
  class Meta:
    ordering = ('name', )
  
  def __str__(self):
    return self.name

class Collection(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  
  created_by = models.ForeignKey(User,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name='collection_creator')
  
  class Meta:
    ordering = ('name', )
  
  def __str__(self):
    return self.name

class DataSource(models.Model):
  id = models.AutoField(primary_key=True)
  uuid = models.CharField(max_length=250)

  name = models.CharField(max_length=500)
  description = models.TextField(null=True, blank=True)
  url = models.CharField(max_length=500, null=True, blank=True)
  source = models.CharField(max_length=100, null=True, blank=True)

  created_by = models.ForeignKey(User,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name='data_source_creator')

  class Meta:
    ordering = ('name', )
  
  def __str__(self):
    return self.name

class PublicationStatus(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=250, unique=True)
