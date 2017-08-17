from django.test import TestCase
from django.urls import reverse

from .models import Card, Meal
import datetime


class MealModelTests(TestCase):

    def test_image_tag(self):
        """
        Testing if image tag is properly created
        """
        tag = Meal(picture='menu/static/menu/pictures/foto.jpg')
        self.assertEqual(tag.image_tag(), '<img src="/static/menu/pictures/foto.jpg" width="50" height="50" />')


def create_meal(id):
    """
    Create a meal with given parameters
    """
    name = "Schabowy"
    description = "kotlet"
    price = 10.00
    preparation_time = '00:05:00'
    vegetarian = True
    picture = None
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
        If only empty card exist.
        """
        create_meal(id=1)
        create_card(id=1, name='Mieso')
        create_card(id=2, name='Empty', empty=True)
        response = self.client.get(reverse('cards'))
        self.assertContains(response, "Menu Cards")
        self.assertQuerysetEqual(response.context['object_list'], ['<Card: Mieso>'])
