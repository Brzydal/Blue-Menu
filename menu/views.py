from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Card


class CardListView(ListView):
    model = Card

    def get_queryset(self):
        qs = super(CardListView, self).get_queryset()
        return qs.filter(meal__isnull=False)


class CardDetailView(DetailView):
    model = Card


