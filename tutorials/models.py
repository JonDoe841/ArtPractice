from django.db import models

from categories.models import Category

class DifficultyChoices(models.TextChoices):
    BEGINNER = 'beginner', 'Beginner'
    INTERMEDIATE = 'intermediate', 'Intermediate'
    ADVANCED = 'advanced', 'Advanced'

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()

    difficulty = models.CharField(
        max_length=20,
        choices=DifficultyChoices.choices,
    )

    estimated_time = models.PositiveIntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    techniques = models.ManyToManyField(
        'Technique',
        related_name='tutorials',
        blank=True,

    )
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Technique(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
