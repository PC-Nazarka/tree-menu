from django.urls import path

from apps.tree.views import DetailMenu, ListMenus

urlpatterns = [
    path("", ListMenus.as_view(), name="menus-list"),
    path("<int:pk>/", DetailMenu.as_view(), name="menu-detail")
]
