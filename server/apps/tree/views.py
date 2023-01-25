from django.views.generic.list import ListView

from apps.tree.models import Menu


class ListMenus(ListView):
    template_name = "tree/list.html"
    context_object_name = "menus"

    def get_queryset(self):
        return Menu.objects.prefetch_related("items").all()
