from django.db import models


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class BaseModel(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)

    objects = CustomManager()

    class Meta:
        abstract = True
