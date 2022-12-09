from django.template import Library

register = Library()


@register.filter('odd')
def get_odd_values(values: list):
    return [x for x in values if x % 2 == 1]

