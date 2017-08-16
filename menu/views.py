from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Card


class CardListView(ListView):
    model = Card

    def get_queryset(self):
        queryset = Card.objects.filter(meal__isnull=False)
        return queryset


class CardDetailView(DetailView):
    model = Card


