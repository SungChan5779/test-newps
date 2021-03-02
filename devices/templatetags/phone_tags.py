from django import template
# from . import modelss

register = template.Library()

@register.simple_tag
def name_value(count):
    name = "phones." + "name_" + str(count)
    print(name)
    return name
