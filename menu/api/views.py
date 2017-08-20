from rest_framework.generics import ListAPIView, RetrieveAPIView

from menu.models import Card
from menu.serializers import CardSerializer


class CardListApiView(ListAPIView):
    queryset = Card.objects.non_empty_cards().prefetch_related('meals')
    serializer_class = CardSerializer


class CardRetrieveApiView(RetrieveAPIView):
    queryset = Card.objects.non_empty_cards()
    serializer_class = CardSerializer
