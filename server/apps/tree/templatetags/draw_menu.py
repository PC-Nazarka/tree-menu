from django import template

register = template.Library()


@register.inclusion_tag("tree/menu.html")
def draw_menu(menu):
    return {"menu": menu}
