from django import template

from apps.tree.models import MenuItem

register = template.Library()


@register.inclusion_tag("tree/menu_item.html")
def draw_item(item_id: int, db_items: list[MenuItem]) -> dict:
    item = list(filter(lambda x: x.id == item_id, db_items))[0]
    items = list(filter(lambda x: x.parent_id == item_id, db_items))
    return {"item": item, "items": items, "db_items": db_items}
