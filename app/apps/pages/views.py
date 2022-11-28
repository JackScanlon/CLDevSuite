from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
  template_name = 'pages/home/index.html'

  def get(self, request):
    return render(request, self.template_name, None)