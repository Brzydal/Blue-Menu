from rest_framework.generics import ListAPIView

from menu.models import Card
from menu.serializers import CardSerializer


class CardListApiView(ListAPIView):
    queryset = Card.objects.with_meals()
    serializer_class = CardSerializer

    # def get_queryset(self):
    #     """
    #     Returns all not empty Menu Cards
    #     """
    #     return super(CardListApiView, self).get_queryset().with_meals()
