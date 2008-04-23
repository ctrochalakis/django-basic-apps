from django import template
from basic.inlines.parser import inlines

register = template.Library()

@register.filter
def render_inlines(value):
  """
  Renders inlines in a ``Post`` by passing them through inline templates.
  
  Template Syntax::
    
    {{ post.body|render_inlines|markdown }}
  
  Inline Syntax (singular)::
    
      <inline type="<app_name>.<model_name>" id="<id>" class="med_left" />
    
  Inline Syntax (plural)::
  
      <inline type="<app_name>.<model_name>" ids="<id>, <id>, <id>" />
  
  An inline template will be used to render the inline. Templates will be
  locaed in the following maner:
  
    ``inlines/<app_name>_<model_name>.html``
  
  The template will be passed the following context:
    
    ``object``
      An object for the corresponding passed id.
  
  or
  
    ``object_list``
      A list of objects for the corresponding ids.
  
  It would be wise to anticipate both object_list and object unless 
  you know for sure one or the other will only be present.
  """
  return inlines(value)

@register.filter
def extract_inlines(value):
  return inlines(value, True)