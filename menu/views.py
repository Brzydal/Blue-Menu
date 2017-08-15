# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Card, Meal

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic.edit import (
    CreateView,
    DeleteView, )
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Shop
from .serializers import ShopSerializer


class CardsView(ListView):
    template_name = 'menu/cards.html'
    model = Card
