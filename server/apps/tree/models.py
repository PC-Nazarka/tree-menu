from django.db import models


class Menu(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="Название меню",
        unique=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self) -> str:
        return f"{self.name}"


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Меню",
    )
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="children",
        verbose_name="Родительский элемент",
    )
    name = models.CharField(
        max_length=128,
        verbose_name="Название элемента",
    )

    class Meta:
        verbose_name = "Элемент Меню"
        verbose_name_plural = "Элементы Меню"

    def __str__(self) -> str:
        return f"{self.name}"
