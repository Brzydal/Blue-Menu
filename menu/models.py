# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import reverse


class Card(models.Model):
    """
    This model represents Menu Card.
    """

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card', kwargs={'pk': self.id})


# class Meal(models.Model):
#     """
#     This model represents Meal.
#     """
#
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=64)
#     description = models.TextField()
#     logo = models.CharField(max_length=256, null=True)
#     main_category = models.ForeignKey(Category)
#     categories = models.CharField(max_length=64, null=True)
#     level = models.IntegerField()
#     lottery = models.BooleanField()
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('shop', kwargs={'pk': self.id})
#
#     def image_tag(self):
#         return u'<img src="%s" width="50" height="50" />' % self.logo
#
#     image_tag.short_description = 'Image'
#     image_tag.allow_tags = True
