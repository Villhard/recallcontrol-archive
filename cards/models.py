from django.db import models


class Card(models.Model):
    front = models.TextField()
    back = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.front[:10]} - {self.back[:10]}"
