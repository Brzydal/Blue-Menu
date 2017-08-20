# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Card, Meal


class MealModelTests(TestCase):
    def test_image_tag_hd(self):
        """
        Testing if image tag is properly created for images from hard drive
        """
        tag = Meal(picture='/static/menu/pictures/foto.jpg')
        self.assertEqual(tag.image_tag(), '<img src="/media/static/menu/pictures/foto.jpg" width="50" height="50" />')

    def test_image_tag_http(self):
        """
        Testing if image tag is properly created for images from hard drive
        """
        tag = Meal(picture='http://static/menu/pictures/foto.jpg')
        self.assertEqual(tag.image_tag(), '<img src="http://static/menu/pictures/foto.jpg" width="50" height="50" />')


def create_meal(id):
    """
    Create a meal with given parameters
    """
    name = "Schabowy"
    description = "kotlet"
    price = 10.00
    preparation_time = '00:05:00'
    vegetarian = True
    picture = 'http://static/menu/pictures/foto.jpg'
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    return Meal.objects.create(id=id,
                               name=name,
                               description=description,
                               price=price,
                               preparation_time=preparation_time,
                               vegetarian=vegetarian,
                               picture=picture,
                               created_at=created_at,
                               updated_at=updated_at)


def create_card(id, name, empty=False):
    """
    Create card with the given parameters
    """
    description = "krolewskie podroby"
    meals = [1, ] if not empty else []
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    return Card.objects.create(id=id,
                               name=name,
                               description=description,
                               meals=meals,
                               created_at=created_at,
                               updated_at=updated_at)


class CardIndexViewTests(TestCase):
    def test_no_cards(self):
        """
        If no cards exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('cards'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "NO CARDS IN DATABASE")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_not_empty_card(self):
        """
        If only not empty card exist.
        """
        create_meal(id=1)
        create_card(id=1, name='Mieso')
        response = self.client.get(reverse('cards'))
        self.assertContains(response, "Menu Cards")
        self.assertQuerysetEqual(response.context['object_list'], ['<Card: Mieso>'])

    def test_empty_card(self):
        """
        If only empty card exist.
        """
        create_card(id=1, name='Empty', empty=True)
        response = self.client.get(reverse('cards'))
        self.assertContains(response, "NO CARDS IN DATABASE")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_empty_card_and_not_empty_card(self):
        """
        If empty and not empty cards exist.
        """
        create_meal(id=1)
        create_card(id=1, name='Mieso')
        create_card(id=2, name='Empty', empty=True)
        response = self.client.get(reverse('cards'))
        self.assertContains(response, "Menu Cards")
        self.assertQuerysetEqual(response.context['object_list'], ['<Card: Mieso>'])


class CardDetailViewTests(TestCase):

    def test_no_card(self):
        """
        If there is no card.
        """
        url = reverse('card', args=([1,]))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_empty_card(self):
        """
        If there is no meals on a card.
        """
        card = create_card(id=1, name='Empty', empty=True)
        url = reverse('card', args=(card.id,))
        response = self.client.get(url)
        self.assertContains(response, 'NO MEALS IN THIS CARD')

    def test_not_empty_card(self):
        """
        If there are some meals on a card.
        """
        meal = create_meal(id=1)
        card = create_card(id=1, name='Mieso', empty=False)
        url = reverse('card', args=(card.id,))
        response = self.client.get(url)
        self.assertContains(response, meal.name)


class CardApiListTests(APITestCase):

    def test_no_card(self):
        """
        If there is no card.
        """
        url = reverse('cards-api-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Card.objects.count(), 0)

    def test_empty_card(self):
        """
        If only empty card exist.
        """
        card = create_card(id=1, name='Empty', empty=True)
        url = reverse('cards-api-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Card.objects.count(), 1)
        self.assertEqual(Card.objects.get().name, card.name)
        self.assertNotContains(response, card.name)

    def test_not_empty_card(self):
        """
        If there is not empty card.
        """
        meal = create_meal(id=1)
        card = create_card(id=1, name='Mieso', empty=False)
        url = reverse('cards-api-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Card.objects.count(), 1)
        self.assertEqual(Card.objects.get().name, card.name)
        self.assertContains(response, card.name)

    def test_empty_card_and_not_empty_card(self):
        """
        If empty and not empty cards exist.
        """
        meal = create_meal(id=1)
        card1 = create_card(id=1, name='Mieso', empty=False)
        card2 = create_card(id=2, name='Empty')
        url = reverse('cards-api-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Card.objects.count(), 2)
        self.assertContains(response, card1.name)
        self.assertContains(response, card2.name)
        

class CardApiRetrieveTests(APITestCase):

    def test_no_card(self):
        """
        If there is no card.
        """
        url = reverse('cards-api-retrieve', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Card.objects.count(), 0)

    def test_empty_card(self):
        """
        If only empty card exist.
        """
        card = create_card(id=1, name='Empty', empty=True)
        url = reverse('cards-api-retrieve', kwargs={'pk': card.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Card.objects.count(), 1)
        self.assertEqual(Card.objects.get().name, card.name)

    def test_not_empty_card(self):
        """
        If there is not empty card.
        """
        meal = create_meal(id=1)
        card = create_card(id=1, name='Mieso', empty=False)
        url = reverse('cards-api-retrieve', kwargs={'pk': card.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Card.objects.count(), 1)
        self.assertEqual(Card.objects.get().name, card.name)
        self.assertContains(response, card.name)

    def test_empty_card_and_not_empty_card(self):
        """
        If empty and not empty cards exist.
        """
        meal = create_meal(id=1)
        card1 = create_card(id=1, name='Mieso', empty=False)
        card2 = create_card(id=2, name='Empty')
        url = reverse('cards-api-retrieve', kwargs={'pk': card1.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Card.objects.count(), 2)
        self.assertContains(response, card1.name)
