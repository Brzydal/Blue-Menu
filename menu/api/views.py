from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from menu.models import Card
from menu.serializers import CardSerializer


class CardListApiView(ListAPIView):
    queryset = Card.objects.all().order_by('id').exclude(meals__isnull=True)
    serializer_class = CardSerializer

    def list(self, request):
        queryset = self.get_queryset()

        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)
