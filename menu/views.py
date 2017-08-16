
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Card, Meal
from .serializers import CardSerializer, MealSerializer


class CardsView(ListView):
    template_name = 'menu/cards.html'
    model = Card

    @staticmethod
    def get_queryset():
        queryset = Card.objects.filter(meal__isnull=False)
        return queryset


class CardView(DetailView):
    template_name = 'menu/card.html'
    model = Card


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


class MealsApiView(APIView):

    @staticmethod
    def get_all():
        try:
            return Meal.objects.all()
        except Meal.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        meals = self.get_all()
        serializer = MealSerializer(meals, many=True, context={"request": request})
        return Response(serializer.data)


