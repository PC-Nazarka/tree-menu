from django import template

register = template.Library()


@register.inclusion_tag("tree/menu_item.html")
def draw_item(item):
    return {"item": item}
