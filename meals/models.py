from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    recipe_link = models.URLField()

    class Meta:
        db_table = 'recipe'


class Ingredient(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        db_table = 'ingredient'


class User(models.Model):
    username = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'user'


class UserGroup(models.Model):
    description = models.CharField(max_length=255)
    recipes = models.ManyToManyField(
        Recipe)
    ingredients = models.ManyToManyField(
        Ingredient)
    users = models.ManyToManyField(
        User)
    # !need to upate this and set it to another user in the group!
    admin = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='group_admin')

    class Meta:
        db_table = 'user_group'

# through models for many to many relationships
