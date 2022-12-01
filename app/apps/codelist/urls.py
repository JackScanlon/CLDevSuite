from django.urls import path, include
from .views import PaginatedCodelist

app_name = 'codelist'

urlpatterns = [
  path('', PaginatedCodelist.as_view(), name='get_codelist'),
]