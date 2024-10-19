from rest_framework.viewsets import ModelViewSet
from cards.models import Card
from api.serializers import CardSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
