from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index_page),
    path('about', views.about_page),
]
