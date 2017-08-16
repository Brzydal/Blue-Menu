from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from menu.models import Card
from menu.serializers import CardSerializer


class CardsApiView(APIView):

    @staticmethod
    def get_all():
        try:
            return Card.objects.all()
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        cards = self.get_all()
        serializer = CardSerializer(cards, many=True, context={"request": request})
        return Response(serializer.data)