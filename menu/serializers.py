from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    meal_count = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'meal', 'meal_count')

    def get_meal_count(self, obj):
        return obj.meal.count()
