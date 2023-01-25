from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TreeConfig(AppConfig):
    """Class-configuration of tree app."""

    name = "apps.tree"
    verbose_name = _("Trees")
