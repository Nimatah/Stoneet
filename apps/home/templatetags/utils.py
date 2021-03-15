from django import template

from apps.orders.models import Order

register = template.Library()


@register.simple_tag
def define(val=None):
    return val


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    return query.urlencode()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

