from django.forms import ModelForm
from cards.models import Card
from django import forms


class CardForm(ModelForm):
    front = forms.CharField(label="Передняя сторона")
    back = forms.CharField(label="Задняя сторона")
    is_active = forms.BooleanField(label="В изучении", initial=True)

    class Meta:
        model = Card
        fields = ["front", "back", "is_active"]
