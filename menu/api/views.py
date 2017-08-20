from rest_framework.generics import ListAPIView, RetrieveAPIView

from menu.models import Card
from menu.serializers import CardSerializer


class CardListAPIView(ListAPIView):
    """
    List API View for Card model
    """
    queryset = Card.objects.non_empty_cards().prefetch_related('meals')
    serializer_class = CardSerializer


class CardRetrieveAPIView(RetrieveAPIView):
    """
    Retrieve API View for Card model
    """
    queryset = Card.objects.non_empty_cards()
    serializer_class = CardSerializer
