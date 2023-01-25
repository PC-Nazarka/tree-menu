from django.contrib import admin

from apps.tree.models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Class representation of Menu model in admin panel."""

    list_display = (
        "name",
    )
    list_filter = (
        "name",
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Class representation of MenuItem model in admin panel."""

    search_fields = (
        "menu",
    )
    list_display = (
        "name",
    )
    list_filter = (
        "name",
    )
