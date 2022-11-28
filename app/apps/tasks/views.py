from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django_celery_results.models import TaskResult
from .tasks import test_celery_task

class CeleryTasks(TemplateView):
    template_name = 'tasks/result.html'

    def run_test_task(self):
      test_celery_task.delay(10)
      return HttpResponseRedirect(reverse('tasks:taskviewer'))

    def post(self, request):
      return self.run_test_task()

    def get(self, request):
      task_list = TaskResult.objects.all()
      return render(request, self.template_name, {'task_list': task_list})

