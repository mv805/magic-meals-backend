from django.db import models

# Create your models here.


class Recipe(models.Model):
    image_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    recipe_link = models.CharField(max_length=255)

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
        Recipe, through='GroupRecipe')
    ingredients = models.ManyToManyField(
        Ingredient, through='UserGroupIngredient')
    users = models.ManyToManyField(
        User, through='GroupUser')
    # !need to upate this and set it to another user in the group!
    admin = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='group_admin')
    
    class Meta:
        db_table = 'user_group'

# through models for many to many relationships


class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'group_user'


class UserGroupIngredient(models.Model):
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_group_ingredient'


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        db_table = 'recipe_ingredient'

class GroupRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'group_recipe'
