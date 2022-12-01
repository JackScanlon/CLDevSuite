import re
import json
import math
import apps.utils.utils as utils
import apps.utils.constants as constants
from apps.utils.decorators import ajax_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from elasticsearch_dsl import Q
from .models import Code, CodingSystem
from .documents import CodeDocument

class PaginatedCodelist(TemplateView):
  def search_by_pattern(self, coding_id, pattern, page):
    matches = Q('bool', must=[Q('match', coding_system__id=coding_id)])
    search = CodeDocument.search() \
      .filter(matches) \
      .filter('regexp', code=pattern)

    hits = search.count()
    start = (page - 1) * constants.CODELIST_PAGE_SIZE
    end = start + constants.CODELIST_PAGE_SIZE
    search = search[start:end].to_queryset()

    return {
      'hits': hits,
      'results': search
    }

  def search_by_term(self, coding_id, term, page):    
    searchterm = Q({'multi_match': {'query': term, 'fields': ['code', 'description'], 'fuzziness': 'AUTO'}})
    matches = Q('bool', must=[Q('match', coding_system__id=coding_id)])
    search = CodeDocument.search() \
      .filter(matches) \
      .filter(searchterm)

    hits = search.count()
    start = (page - 1) * constants.CODELIST_PAGE_SIZE
    end = start + constants.CODELIST_PAGE_SIZE
    search = search[start:end].to_queryset()

    return {
      'hits': hits,
      'results': search
    }
  
  def run_query(self, coding_id, query, page):
    if query.lower().startswith('wildcard:'):
      matches = re.search('^wildcard:(.*)', query)
      return self.search_by_pattern(coding_id, matches.group(1), page)
    
    return self.search_by_term(coding_id, query, page)
  
  @method_decorator(ajax_required)
  def get(self, request):
    return render(request, '400.html', status=400)

  def post(self, request):
    body = utils.get_request_body(request.body);

    id = utils.parse_int(utils.get_content(body, 'id', 0))
    coding_system = utils.get_coding_system_by_id(id)

    page = utils.parse_int(utils.get_content(body, 'page', 0))
    page = max(page, 1)

    query = utils.get_content(body, 'query')
    if query is not None and query != '':
      response = self.run_query(id, query, page)

      return JsonResponse({
        'coding_id': id,
        'coding_name': coding_system.name,
        'page': page,
        'pages': math.ceil(response['hits'] / constants.CODELIST_PAGE_SIZE),
        'total': response['hits'],
        'codes': [model_to_dict(obj) for obj in response['results']]
      })

    else:
      codelist = utils.get_codelist_by_coding_system(coding_system)
      codes = codelist.codes.all()
      pages = Paginator(codes, constants.CODELIST_PAGE_SIZE)
      objs = pages.page(page)
      objs = [model_to_dict(obj) for obj in objs]

      return JsonResponse({
        'coding_id': id,
        'coding_name': coding_system.name,
        'page': page,
        'pages': pages.num_pages,
        'total': codes.count(),
        'codes': objs
      })