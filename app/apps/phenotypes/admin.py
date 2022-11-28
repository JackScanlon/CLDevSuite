from django.contrib import admin
from .models import PhenotypeType, Phenotype

@admin.register(PhenotypeType)
class PhenotypeTypeAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']

@admin.register(Phenotype)
class PhenotypeAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'status', 'owner', 'organisation']
