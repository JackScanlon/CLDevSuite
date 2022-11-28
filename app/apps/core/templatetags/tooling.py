from django import template

register = template.Library()

@register.filter
def within(value, arg):
  return arg in value
