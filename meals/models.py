from django.db import models

# Create your models here.
class User(models.Model):
    display_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'

class UserGroup(models.Model):
    group_name = models.CharField(max_length=255)
    description = models.TextField()
    users = models.ManyToManyField(User)

    class Meta:
        db_table = 'user_group'

class Food(models.Model):

    MAJOR_THREAT = 'Major'
    CAUTION_ONLY = 'Caution'
    NOT_ASSESSED = 'NA'

    THREAT_LEVELS = [
        (MAJOR_THREAT, 'Major Threat'),
        (CAUTION_ONLY, 'Caution only'),
        (NOT_ASSESSED, 'Not Assesed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    threat_level = models.CharField(
        max_length=255,
        choices=THREAT_LEVELS,
        default=NOT_ASSESSED,
    )
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'food'


class Allergen(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    major_allergen = models.BooleanField(default=False)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergen'







# through models for many to many relationships
