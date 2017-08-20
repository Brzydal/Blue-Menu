from rest_framework.generics import ListAPIView

from menu.models import Card
from menu.serializers import CardSerializer


class CardListApiView(ListAPIView):
    queryset = Card.objects.non_empty_cards()
    serializer_class = CardSerializer

