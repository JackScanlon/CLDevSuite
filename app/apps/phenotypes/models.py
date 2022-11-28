from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField, DateTimeRangeField
from simple_history.models import HistoricalRecords
from ..core.models import Brand, PublicationStatus, DataSource, Collection, Tag
from ..concepts.models import CodingSystem, Concept
from ..organisation.models import Organisation

User = get_user_model()

class PhenotypeGender:
  UNISEX = 1
  MALE   = 2
  FEMALE = 3
  GENDER_CHOICES = ((UNISEX, 'Male/Female'), (MALE, 'Male'), (FEMALE, 'Female'))

class PhenotypeType(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=250, unique=True)
  
  class Meta:
    ordering = ('name', )

  def __str__(self):
    return self.name

class Phenotype(models.Model):
  id = models.CharField(primary_key=True, editable=False, max_length=50)
  status = models.ForeignKey(PublicationStatus, on_delete=models.SET_NULL, null=True, related_name='phenotype_publication_status')
  brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='related_phenotype_brand')

  created = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='phenotype_creator')
  
  updated = models.DateTimeField(auto_now_add=True)
  updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='phenotype_updated_by')

  owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='phenotypes_owner')
  organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True, related_name='phenotypes_organisation')

  uuid = models.CharField(max_length=250, null=True, blank=True)
  phenoflowid = models.CharField(max_length=100, null=True, blank=True)

  name = models.CharField(max_length=250)
  valid_date_range = DateTimeRangeField()
  author = models.CharField(max_length=1000)
  sex = models.IntegerField(choices=PhenotypeGender.GENDER_CHOICES, default=PhenotypeGender.UNISEX)
  description = models.TextField(null=True, blank=True)
  implementation = models.TextField(null=True, blank=True)
  source_reference = models.CharField(max_length=250, null=True, blank=True)
  citation_requirements = models.CharField(max_length=250, null=True, blank=True)
  
  is_published = models.BooleanField(null=True, default=False)
  primary_publication = models.IntegerField(blank=True, null=True)
  publication_urls = ArrayField(models.URLField(), blank=True, null=True)
  
  validation_performed = models.BooleanField(null=True, default=False)
  validation = models.TextField(null=True, blank=True)

  concepts = models.ManyToManyField(Concept, related_name='related_concepts', blank=True)

  type = models.ForeignKey(PhenotypeType, on_delete=models.CASCADE, related_name='related_type')
  tags = models.ManyToManyField(Tag, related_name='related_tags', blank=True)
  collections = models.ManyToManyField(Collection, related_name='related_collections', blank=True)
  data_sources = models.ManyToManyField(DataSource, related_name='related_data_sources', blank=True)
  terminology = models.ManyToManyField(CodingSystem, related_name='related_concepts_coding_systems', blank=True)

  history = HistoricalRecords()

  def save(self, *args, **kwargs):
    self.id = f'PH{Phenotype.objects.count()}'
    super(Phenotype, self).save(*args, **kwargs)
  
  def save_without_historical_record(self, *args, **kwargs):
    self.skip_history_when_saving = True
    try:
      ret = self.save(*args, **kwargs)
    finally:
      del self.skip_history_when_saving
    return ret
  
  class Meta:
    ordering = ('name', )
    permissions = (
      ('can_approve', 'Can approve phenotype'),
    )

  def __str__(self):
    return self.name

class PhenotypeDraft(models.Model):
  id = models.CharField(primary_key=True, editable=False, max_length=50)
  brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='related_phenotype_draft_brand')

  created = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='phenotype_draft_creator')

  owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='phenotype_draft_owner')
  organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True, related_name='phenotype_draft_organisation')

  name = models.CharField(max_length=250)
  data = models.JSONField(blank=True, null=True)

  def save(self, *args, **kwargs):
    self.id = f'PH{PhenotypeDraft.objects.count()}'
    super(PhenotypeDraft, self).save(*args, **kwargs)
  
  class Meta:
    ordering = ('name', )

  def __str__(self):
    return self.name
