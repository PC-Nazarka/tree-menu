DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.forms",
]

LOCAL_APPS = [
    "apps.tree.apps.TreeConfig",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
