# Generated by Django 4.1.5 on 2023-02-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_alter_food_allergens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='allergens',
        ),
        migrations.AddField(
            model_name='food',
            name='allergens',
            field=models.ManyToManyField(to='meals.allergen'),
        ),
    ]
