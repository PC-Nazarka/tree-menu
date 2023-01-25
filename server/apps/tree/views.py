from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.tree.models import Menu


class ListMenus(ListView):
    template_name = "tree/list_menu.html"
    context_object_name = "menus"

    def get_current_menus(self):
        menus = self.request.GET.get("menu", None)
        return menus.split(",") if menus else menus

    def get_queryset(self):
        query = Menu.objects.prefetch_related("items")
        if menus := self.get_current_menus():
            return query.filter(name__in=menus)
        return query.all()


class DetailMenu(DetailView):
    template_name = "tree/detail_menu.html"
    context_object_name = "menu"
    queryset = Menu.objects.all()
