from django import template

register = template.Library()

@register.filter(name='StringToList')
def string_to_list(value):
    return value.split(",")

@register.filter(name='IsURL')
def is_url(value):
    check_string = value.split(":")[0]
    if (check_string == "http" or check_string == "https"):
        return f'<a href="{value}" target="_blank">{value}</a>'
    return value