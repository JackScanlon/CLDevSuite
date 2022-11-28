from django.urls import path, include
from .views import CeleryTasks

app_name = 'tasks'

urlpatterns = [
    path('', CeleryTasks.as_view(), name='taskviewer'),
    path('run-task/', CeleryTasks.run_test_task, name='run_test_task')
]