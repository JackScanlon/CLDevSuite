import json
import apps.utils.utils as utils
from django.views.generic import TemplateView
from django.shortcuts import render

class CreatePhenotypeView(TemplateView):
  template_name = 'phenotype/create_phenotype.html'

  def get(self, request):
    context = {
      'phenotype_types': utils.get_phenotype_types_by_brand(request, jsonify=True),
      'tags': utils.get_tags_by_brand(request, jsonify=True),
      'collections': utils.get_collections_by_brand(request, jsonify=True),
      'coding_system': utils.get_coding_system_by_brand(request, jsonify=True),
      'data_sources': utils.get_data_sources_by_brand(request, jsonify=True),
    }

    return render(request, self.template_name, context=context)

class PhenotypeHomeView(TemplateView):
  template_name = 'phenotype/index.html'

  def get(self, request):
    context = {
      
    }

    return render(request, self.template_name, context=context)