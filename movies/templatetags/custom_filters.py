from django import template

register = template.Library()

@register.filter
def num_range(num):
    return range(num)

@register.filter
def get_item(list_, index):
    return list_[index]