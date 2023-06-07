from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('/password', views.user_profile_password, name='user_profile_password'),
    path('/user_favorite_grid', views.user_favorite_grid, name='user_favorite_grid'),
    path('/user_favorite_list', views.user_favorite_list, name='user_favorite_list'),

]
