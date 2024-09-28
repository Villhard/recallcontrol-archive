from datetime import timedelta

from django.db import models
from django.utils import timezone


class StudyCard(models.Manager):
    def get_queryset(self):
        one_hour_ago = timezone.now() - timedelta(minutes=1)
        return (
            super().get_queryset().filter(is_active=True, updated_at__lt=one_hour_ago)
        )


class Card(models.Model):
    front = models.TextField()
    back = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recalled_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    study_objects = StudyCard()

    def __str__(self):
        return f"{self.front[:10]} - {self.back[:10]}"
