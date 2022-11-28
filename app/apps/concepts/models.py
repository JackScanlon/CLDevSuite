from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords
from ..codelist.models import Code, CodingSystem

User = get_user_model()

class Component(models.Model):
  id = models.AutoField(primary_key=True)
  source = models.CharField(max_length=250)
  codes = models.ManyToManyField(Code, related_name='related_codes', blank=True, through='CodeRule')

  class Meta:
    ordering = ('source', )
  
  def __str__(self):
    return self.source

class CodeRule(models.Model):
  code = models.ForeignKey(Code, on_delete=models.CASCADE)
  component = models.ForeignKey(Component, on_delete=models.CASCADE)
  rule = models.BooleanField(null=True, default=True)

  class Meta:
    ordering = ('code', )
  
  def __str__(self):
    return f'CodeRule<{self.code}, {self.rule}>'

class Concept(models.Model):
  id = models.CharField(primary_key=True, editable=False, max_length=50)
  name = models.CharField(max_length=250)

  created = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='concept_creator')
  created_from = models.ForeignKey('phenotypes.Phenotype', on_delete=models.SET_NULL, null=True, related_name='original_phenotype')

  coding_system = models.ForeignKey(CodingSystem, on_delete=models.SET_NULL, null=True, related_name='coding_system_data')
  components = models.ManyToManyField(Component, related_name='related_components', blank=True)

  def save(self, *args, **kwargs):
    self.id = f'C{Concept.objects.count()}'
    super(Concept, self).save(*args, **kwargs)
  
  class Meta:
    ordering = ('name', )

  def __str__(self):
    return self.name
