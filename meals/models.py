from django.db import models

# Create your models here.


class Recipe(models.Model):
    image_url = models.CharField()
    title = models.CharField()
    description = models.TextField()
    recipe_link = models.CharField()


class Ingredient(models.Model):
    title = models.CharField(max_length=255)


class User(models.Model):
    username = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class GroupAdmin(models.Model):
    admin_title = models.CharField(
        max_length=255, default='Group Administrator')


class UserGroup(models.Model):
    description = models.CharField(max_length=255)
    recipes = models.ManyToManyField(
        Recipe, on_delete=models.PROTECT, through='GroupRecipe')
    ingredients = models.ManyToManyField(
        Ingredient, on_delete=models.PROTECT, through='UserGroupIngredient')
    users = models.ManyToManyField(
        User, through='GroupUser', on_delete=models.PROTECT)
    admin = models.OneToOneField(
        GroupAdmin, default=users[0], on_delete=models.SET_DEFAULT)

# through models for many to many relationships


class GroupUser(models.Model):
    pass


class UserGroupIngredient(models.Model):
    pass


class RecipeIngredient(models.Model):
    pass


class GroupRecipe(models.Model):
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
