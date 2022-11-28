from django.contrib import admin
from .models import Brand, Tag, Collection, DataSource, PublicationStatus

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
  list_display = ['id', 'site_title', 'name', 'owner']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'created_by']

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'created_by']

@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'created_by', 'url']

@admin.register(PublicationStatus)
class PublicationStatus(admin.ModelAdmin):
  list_display = ['id', 'name']

