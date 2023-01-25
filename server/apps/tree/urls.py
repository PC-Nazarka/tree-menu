from django.urls import path

from apps.tree.views import ListMenus

urlpatterns = [
    path("", ListMenus.as_view())
]
