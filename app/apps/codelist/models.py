from django.db import models

class Code(models.Model):
  id = models.AutoField(primary_key=True)
  code = models.CharField(max_length=250, null=False)
  description = models.TextField(null=False)

  class Meta:
    ordering = ('code', )
  
  def __str__(self):
    return self.code

class CodingSystem(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=250)

  class Meta:
    ordering = ('name', )
  
  def __str__(self):
    return self.name

class CodeList(models.Model):
  id = models.AutoField(primary_key=True)
  coding_system = models.ForeignKey(CodingSystem, on_delete=models.SET_NULL, null=True, related_name='related_coding_system')
  codes = models.ManyToManyField(Code, related_name='codelist', blank=True)

  class Meta:
    ordering = ('id', )
  
  def __str__(self):
    return self.coding_system.name