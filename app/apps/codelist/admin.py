from django.contrib import admin
from .models import CodingSystem, CodeList

@admin.register(CodingSystem)
class CodingSystemAdmin(admin.ModelAdmin):
  list_display = ['name']

@admin.register(CodeList)
class CodeListAdmin(admin.ModelAdmin):
  list_display = ['coding_system', 'num_codes']

  def num_codes(self, obj):
    return obj.codes.count()