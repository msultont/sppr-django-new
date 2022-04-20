from django import template

register = template.Library()

@register.filter(name='StringToList', is_safe=True)
def string_to_list(value):
    
    return value.split(",")