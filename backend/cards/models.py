from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Card(models.Model):
    front = models.TextField()
    back = models.TextField()
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")

    def __str__(self):
        return f"{self.front[:10]} - {self.back[:10]}"
