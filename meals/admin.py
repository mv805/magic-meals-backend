from django.contrib import admin
from django.db.models import Count
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'display_name']
    search_fields = ['email__istartswith', 'display_name__istartswith']

class MajorAllergenFilter(admin.SimpleListFilter):
    title = 'is Major Allergen'
    parameter_name = 'major_allergen'

    def lookups(self, request, model_admin):
        return [
            ('True', 'Major Allergen')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'True':
            return queryset.filter(major_allergen__exact=True)

@admin.register(models.Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ['title', 'major_allergen', 'user_group']
    list_filter = ['user_group', MajorAllergenFilter]
    search_fields = ['title']


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'threat_level', 'user_group' ]
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
