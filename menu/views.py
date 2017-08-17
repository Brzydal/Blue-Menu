import coreapi
from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Card


class CardListView(ListView):
    model = Card
    paginate_by = 5

    def get_queryset(self):
        """
        Returns all not empty Menu Cards
        """
        return super(CardListView, self).get_queryset().with_meals()


class CardDetailView(DetailView):
    model = Card


class FinalView(View):

    def get(self, request):
        """
        Rendering final.html template with API data as a context.
        """
        client = coreapi.Client()
        schema = client.get('http://127.0.0.1:8000/cardsAPI/')
        ctx = {'result': schema}
        return render(request, 'menu/final.html', ctx)
        # return render(request, 'menu/final.html')
