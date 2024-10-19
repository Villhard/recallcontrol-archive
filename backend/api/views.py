from rest_framework import viewsets
from cards.models import Card
from api.serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
