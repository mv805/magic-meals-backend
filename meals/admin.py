from django.contrib import admin
from django.db.models import Count
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'display_name']


@admin.register(models.Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ['title', 'major_allergen', 'user_group']


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'threat_level', 'user_group' ]
    # ordering = ['title', 'user_group']
    filter_horizontal = ('allergens',)

@admin.register(models.UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'members']
    filter_horizontal = ('users',)

    def members(self, user_group):
        return user_group.members
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(members=Count('users'))
        return queryset

    members.admin_order_field = 'members'
