# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from menu.models import Card, Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """
    Model Meal registered in Django Admin
    """
    readonly_fields = ['image_tag',
                       ]
    list_display = ['id',
                    'name',
                    'description',
                    'price',
                    'preparation_time',
                    'vegetarian',
                    'picture',
                    'created_at',
                    'updated_at',
                    'image_tag']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """
    Model Card registered in Django Admin
    """
    list_display = ['id',
                    'name',
                    'description',
                    'created_at',
                    'updated_at']
