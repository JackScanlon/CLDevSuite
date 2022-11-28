from django.views.generic import TemplateView
from django.shortcuts import render

class CreatePhenotypeView(TemplateView):
  template_name = 'phenotype/create_phenotype.html'

  def get(self, request):
    return render(request, self.template_name, None)

class PhenotypeHomeView(TemplateView):
  template_name = 'phenotype/index.html'

  def get(self, request):
    return render(request, self.template_name, None)