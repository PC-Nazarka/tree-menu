from django import template
from django.shortcuts import get_object_or_404

from apps.tree.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_name: str):
    return get_object_or_404(
        Menu.objects.prefetch_related("items").all(),
        name=menu_name,
    )
