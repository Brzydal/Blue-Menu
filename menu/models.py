from django.db import models
from django.shortcuts import reverse


class Meal(models.Model):
    """
    This model represents Meal.
    """
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.DurationField()
    vegetarian = models.BooleanField()
    picture = models.ImageField(upload_to='menu/static/menu/pictures', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal', kwargs={'pk': self.id})

    def image_tag(self):
        directory = str(self.picture)
        return '<img src="%s" width="50" height="50" />' % directory[4:]

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class CardQuerySet(models.QuerySet):
    """
    This is QuerySet manager for Card model.
    """
    def with_meals(self):
        """
        Returns all not empty Menu Cards
        """
        return self.exclude(meals__isnull=True)


class Card(models.Model):
    """
    This model represents Menu Card.
    """

    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    meals = models.ManyToManyField(Meal, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CardQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card', kwargs={'pk': self.id})

    def get_meals_count(self):
        return self.meals.count()
