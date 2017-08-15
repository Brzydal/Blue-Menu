# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from menu.models import Card, Meal


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Card._meta.fields]
    # Description of List in Admin
    # list_display = \
    #     ['id', 'name', 'description', 'image_tag', 'main_category', 'level', 'lottery', 'date_created', 'date_updated']
    #
    # list_filter = ('main_category', 'lottery',)
    # list_search = ('name',)
    # list_editable = ('description',)
    # ordering = ('id', 'level', 'date_created', 'date_updated')
    # list_display_links = ('name',)
    #
    # # Description of Form Edit in Admin
    # readonly_fields = ['date_created', 'date_updated']


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Meal._meta.fields]
    # Description of List in Admin
    # list_display = ['id', 'name', 'visible']
    # list_filter = ('visible',)
    # list_search = ('name',)
    # ordering = ('id',)
    # list_display_links = ('name',)
