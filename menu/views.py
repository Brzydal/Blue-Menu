# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Card


class CardsView(ListView):
    template_name = 'menu/cards.html'
    model = Card


class CardView(DetailView):
    template_name = 'menu/card.html'
    model = Card
