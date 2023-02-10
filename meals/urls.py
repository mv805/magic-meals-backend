from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/all-groups/', views.all_user_group_list, name='all-groups'),
    path('users/all-users/', views.UserList.as_view(), name='all-users'),
    path('users/user-detail/<int:id>/',
         views.UserDetail.as_view(), name='user-detail'),
]
