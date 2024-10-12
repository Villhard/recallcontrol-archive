from django.forms import ModelForm
from cards.models import Card
from django import forms


class CardForm(ModelForm):
    front = forms.CharField()
    back = forms.CharField()

    class Meta:
        model = Card
        fields = ["front", "back", "is_active"]
