from django.contrib import admin
from .models import Organisation

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'created', 'owner', 'num_members']

  def num_members(self, obj):
    return obj.members.count()

