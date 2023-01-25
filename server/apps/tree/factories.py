from factory import Faker, SubFactory, django

from apps.tree.models import Menu, MenuItem


class MenuFactory(django.DjangoModelFactory):
    name = Faker(
        "pystr",
        min_chars=5,
        max_chars=10,
    )

    class Meta:
        model = Menu
        django_get_or_create = ["name"]


class MenuItemFactory(django.DjangoModelFactory):
    name = Faker(
        "pystr",
        min_chars=5,
        max_chars=10,
    )
    menu = SubFactory(MenuFactory)
    parent = None

    class Meta:
        model = MenuItem
        django_get_or_create = ["name"]
