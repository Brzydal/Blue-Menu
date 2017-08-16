from django.contrib import admin
from menu.models import Card, Meal


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'meal', 'created_at', 'updated_at']


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'preparation_time', 'vegetarian', 'image_tag' 'created_at', 'updated_at']
    readonly_fields = ('image_tag',)

