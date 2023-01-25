from apps.tree.factories import MenuFactory, MenuItemFactory

COUNT_MENUS = 5
COUNT_MENU_ITEMS = 3


def run():
    """Generate example data."""
    menus = MenuFactory.create_batch(size=COUNT_MENUS)
    for menu in menus:
        items = MenuItemFactory.create_batch(
            menu=menu,
            size=COUNT_MENU_ITEMS,
        )
        for item in items:
            MenuItemFactory.create_batch(
                menu=menu,
                parent=item,
                size=COUNT_MENU_ITEMS,
            )
