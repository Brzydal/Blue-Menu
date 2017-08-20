# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import coreapi
from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Card


class CardListView(ListView):
    model = Card
    paginate_by = settings.PAGE_SIZE

    def get_queryset(self):
        """
        Returns all not empty Menu Cards
        """
        return super(CardListView, self).get_queryset().non_empty_cards()


class CardDetailView(DetailView):
    model = Card

    def get_queryset(self):
        """
        Returns details of a card with given id.
        """
        return super(CardDetailView, self).get_queryset().prefetch_related('meals')


class FinalView(View):
    def get(self, request):
        client = coreapi.Client()
        schema = client.get(settings.CARDS_API_URL)
        paginator = Paginator(schema, settings.PAGE_SIZE)

        page = request.GET.get('page')
        try:
            cards = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            cards = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            cards = paginator.page(paginator.num_pages)

        return render(request, 'menu/final.html', {'cards': cards})
