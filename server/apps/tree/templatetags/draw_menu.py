from django import template
from django.shortcuts import get_object_or_404

from apps.tree.models import Menu

register = template.Library()


@register.inclusion_tag("tree/menu.html")
def draw_menu(menu_name: str) -> dict:
    menu = get_object_or_404(
        Menu.objects.prefetch_related("items"),
        name=menu_name,
    )
    db_items = list(menu.items.all())
    return {"menu": menu, "items": db_items}
