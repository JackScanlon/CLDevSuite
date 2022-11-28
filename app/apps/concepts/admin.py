from django.contrib import admin
from .models import Concept, Component

@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'created', 'coding_system', 'num_components']

  def num_components(self, obj):
    return obj.components.count()

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
  list_display = ['id', 'source', 'num_codes']

  def num_codes(self, obj):
    return obj.codes.count()

