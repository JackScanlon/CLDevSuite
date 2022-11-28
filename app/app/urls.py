from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.pages.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('tasks/', include('apps.tasks.urls')),
    path('phenotypes/', include('apps.phenotypes.urls')),
    path('admin/', admin.site.urls),
]
