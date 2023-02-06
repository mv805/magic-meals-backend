from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/all-groups/', views.all_user_group_list, name='all-groups'),
    path('users/all-users/', views.all_users_list, name='all-users'),
    path('users/user-detail/<int:id>/', views.user_detail, name='user-detail'),
]
