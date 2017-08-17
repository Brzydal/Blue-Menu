from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    meals_count = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'meals', 'meals_count']

    def get_meals_count(self, obj):
        return obj.meals.count()
