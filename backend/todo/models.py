from django.conf import settings
from django.db import models


class Todo(models.Model):

    title = models.CharField(max_length=64, null=False)
    description = models.TextFiel(null=True)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="todo",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_add=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} - {self.title}'
