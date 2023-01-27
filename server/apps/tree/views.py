from typing import Optional

from django.db.models import QuerySet
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from apps.tree.models import Menu

QUERY_PARAM_MENU = "menu"


class ListMenus(TemplateView):
    template_name = "tree/list_menu.html"

    def get_current_menus(self) -> Optional[list[str]]:
        menus = self.request.GET.get(QUERY_PARAM_MENU, None)
        return menus.split(",") if menus else menus

    def get_queryset(self) -> QuerySet:
        query = Menu.objects
        if menus := self.get_current_menus():
            return query.filter(name__in=menus)
        return query.all()

    def get_context_data(self, **kwargs) -> dict:
        return {"menus": self.get_queryset()}


class DetailMenu(DetailView):
    template_name = "tree/detail_menu.html"
    context_object_name = "menu"
    queryset = Menu.objects.all()
