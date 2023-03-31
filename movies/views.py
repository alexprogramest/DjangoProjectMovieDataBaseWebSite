from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def the_movie_page(request, movie_id):
    return HttpResponse(f"<h3>Сторінка фільму №{movie_id}</h3>")