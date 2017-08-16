from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from .models import Card


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


