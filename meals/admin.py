from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'display_name']


@admin.register(models.Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ['title', 'user_group']


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'user_group']
    filter_horizontal = ('allergens',)

@admin.register(models.UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ['group_name']
    filter_horizontal = ('users',)
