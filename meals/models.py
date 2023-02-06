from django.db import models

# Create your models here.
class User(models.Model):
    display_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.email
    class Meta:
        db_table = 'user'
        ordering = ['email']

class UserGroup(models.Model):
    group_name = models.CharField(max_length=255)
    description = models.TextField()
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.group_name
    class Meta:
        db_table = 'user_group'
class Allergen(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    major_allergen = models.BooleanField(default=False)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    class Meta:
        db_table = 'allergen'

class Food(models.Model):

    MAJOR_THREAT = 'Major'
    CAUTION_ONLY = 'Caution'
    NOT_ASSESSED = 'NA'
    NO_KNOWN_THREAT = 'None'

    THREAT_LEVELS = [
        (MAJOR_THREAT, 'Major Threat'),
        (CAUTION_ONLY, 'Caution Only'),
        (NOT_ASSESSED, 'Not Assesed'),
        (NO_KNOWN_THREAT, 'No Known Threat'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    allergens = models.ManyToManyField(Allergen, blank=True)
    threat_level = models.CharField(
        max_length=255,
        choices=THREAT_LEVELS,
        default=NOT_ASSESSED,
    )
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    ordering = ['title']

    def __str__(self) -> str:
        return self.title
    class Meta:
        db_table = 'food'








# through models for many to many relationships
