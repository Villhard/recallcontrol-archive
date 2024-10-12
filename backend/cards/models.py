from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class StudyCard(models.Manager):
    def get_queryset(self):
        one_hour_ago = timezone.now() - timedelta(minutes=1)
        return (
            super().get_queryset().filter(is_active=True, updated_at__lt=one_hour_ago)
        )

    class Meta:
        ordering = ["recalled_at"]


class Card(models.Model):
    front = models.TextField()
    back = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recalled_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")

    objects = models.Manager()
    study_objects = StudyCard()

    def __str__(self):
        return f"{self.front[:10]} - {self.back[:10]}"
