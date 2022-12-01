import json
import apps.utils.constants as constants
from django.apps import apps
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

Brand = apps.get_model('core', 'Brand')
Tag = apps.get_model('core', 'Tag')
Collection = apps.get_model('core', 'Collection')
DataSource = apps.get_model('core', 'DataSource')
CodingSystem = apps.get_model('codelist', 'CodingSystem')
PhenotypeType = apps.get_model('phenotypes', 'PhenotypeType')
CodeList = apps.get_model('codelist', 'CodeList')

def parse_int(value, default=0):
  try:
    return int(value)
  except ValueError:
    return default

def get_request_body(body):
  try:
    body = body.decode('utf-8');
    body = json.loads(body)
    return body
  except:
    return None

def get_content(body, key, default=None):
  if key in body:
    return body[key]
  return default

def jsonify_objects(objects, remove_userdata=True):
  result = []
  for obj in objects:
    instance = model_to_dict(obj)
    
    if remove_userdata:
      userdata = {str(field.related_model):field.name for field in obj._meta.local_fields if field.is_relation}
      userdata = [field for model, field in userdata.items() if model in constants.USERDATA]
      for field in userdata:
        instance.pop(field, None)
    
    result.append(instance)

  return json.dumps(result)

def get_brands(jsonify=True):
  objects = Brand.objects.all()
  if jsonify:
    return jsonify_objects(objects)
  return objects

def get_phenotype_types_by_brand(request, jsonify=False):
  objects = PhenotypeType.objects.all()
  if jsonify:
    return jsonify_objects(objects)
  return objects

def get_tags_by_brand(request, jsonify=False):
  objects = Tag.objects.all()
  if jsonify:
    return jsonify_objects(objects)
  return objects

def get_collections_by_brand(request, jsonify=False):
  objects = Collection.objects.all()
  if jsonify:
    return jsonify_objects(objects)
  return objects

def get_coding_system_by_brand(request, jsonify=False):
  objects = CodingSystem.objects.all()
  if jsonify:
    return jsonify_objects(objects)
  return objects

def get_data_sources_by_brand(request, jsonify=False):
  objects = DataSource.objects.all()
  if jsonify:
    return jsonify_objects(objects)
  return objects

def get_codelist_by_coding_system(coding_system):
  return get_object_or_404(CodeList, coding_system=coding_system);

def get_coding_system_by_id(id):
  return get_object_or_404(CodingSystem, pk=id)
