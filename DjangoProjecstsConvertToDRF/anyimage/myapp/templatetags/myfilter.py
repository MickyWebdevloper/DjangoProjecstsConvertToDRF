from django import template

register = template.Library()


@register.filter(name='remove_special')
def remove_chars(value, arg):
    for charactor in arg:
        value = value.replace(charactor, '')
    return value
