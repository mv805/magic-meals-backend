# Generated by Django 4.1.5 on 2023-02-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_remove_food_allergens_food_allergens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='threat_level',
            field=models.CharField(choices=[('Major', 'Major Threat'), ('Caution', 'Caution Only'), ('NA', 'Not Assesed'), ('None', 'No Known Threat')], default='NA', max_length=255),
        ),
    ]
