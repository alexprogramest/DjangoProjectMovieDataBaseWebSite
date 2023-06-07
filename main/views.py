from django.shortcuts import render
from movies.models import MovieGenre, TheMovie
from celebrities.models import Actor
from django.http import HttpResponse


# Create your views here.
def index(request):
    all_movies = TheMovie.objects.all()
    # for one_movie in all_movies:
    #     print(one_movie.genres.all())
    five_celebrities = Actor.objects.all()[:5]
    # print(five_actors)
    return render(request, 'main/index.html', {"all_movies": all_movies, "selected_celebrities": five_celebrities})
