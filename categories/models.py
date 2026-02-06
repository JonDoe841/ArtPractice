from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    order = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name