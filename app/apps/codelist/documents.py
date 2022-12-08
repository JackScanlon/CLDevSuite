from django.apps import apps
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import CodeList, CodingSystem, Code

@registry.register_document
class CodeDocument(Document):
  coding_system = fields.ObjectField(properties={
    'id': fields.IntegerField(),
    'name': fields.TextField(),
  })

  class Index:
    name = 'codes'
    settings = {'number_of_shards': 1, 'number_of_replicas': 1}

  class Django:
    model = Code
    fields = ['code', 'description']
    related_models = [CodingSystem]

  def get_queryset(self):
    return super(CodeDocument, self).get_queryset().select_related('coding_system')

  def get_instances_from_related(self, related_instance):
    if isinstance(related_instance, CodingSystem):
      return related_instance.related_coding_system
