from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.views import View
from .models import Card
import coreapi


class CardListView(ListView):
    model = Card

    def get_queryset(self):
        qs = super(CardListView, self).get_queryset()
        return qs.exclude(meal__isnull=True)


class CardDetailView(DetailView):
    model = Card


class FinalView(View):

    def get(self, request):
        client = coreapi.Client()
        schema = client.get('http://127.0.0.1:8000/cardsAPI/')
        ctx = {'result': schema}
        return render(request, 'menu/final.html', ctx)


