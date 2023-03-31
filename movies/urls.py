from django.urls import path, include

from . import views

urlpatterns = [
    path('/<movie_id>', views.the_movie_page),
]
