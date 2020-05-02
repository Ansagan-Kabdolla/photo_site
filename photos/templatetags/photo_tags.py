from django import template

register = template.Library()

@register.filter
def cut(subservice, s):
    return subservice.filter(basic_service=s)