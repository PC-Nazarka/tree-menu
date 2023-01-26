from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from apps.tree.models import Menu


class ListMenus(TemplateView):
    template_name = "tree/list_menu.html"

    def get_current_menus(self):
        menus = self.request.GET.get("menu", None)
        return menus.split(",") if menus else menus

    def get_queryset(self):
        query = Menu.objects
        if menus := self.get_current_menus():
            return query.filter(name__in=menus)
        return query.all()

    def get_context_data(self, **kwargs):
        return {"menus": self.get_queryset()}


class DetailMenu(DetailView):
    template_name = "tree/detail_menu.html"
    context_object_name = "menu"
    queryset = Menu.objects.all()
