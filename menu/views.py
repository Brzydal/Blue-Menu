import coreapi

from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .constants import Constants
from .models import Card


class CardListView(ListView):
    model = Card
    paginate_by = Constants.page_size

    def get_queryset(self):
        """
        Returns all not empty Menu Cards
        """
        return super(CardListView, self).get_queryset().with_meals()


class CardDetailView(DetailView):
    model = Card


class FinalView(View):
    paginate_by = 1

    def get(self, request):
        """
        Rendering final.html template with API data as a context.
        """
        client = coreapi.Client()
        schema = client.get(Constants.cards_api_url)
        ctx = {'result': schema}
        return render(request, 'menu/final.html', ctx)
        # return render(request, 'menu/final.html')
