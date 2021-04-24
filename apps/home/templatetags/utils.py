from django import template

register = template.Library()


@register.simple_tag
def define(val=None):
    return val


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    return f'?{query.urlencode()}'


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def order_state_lt(order, state):
    return order.state_lt(state)


@register.filter
def user_participated_in_auction(auction, user):
    return auction.has_user_participated(user)
