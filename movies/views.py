from django.shortcuts import render, redirect
from .models import MovieGenre, TheMovie


def get_appropriate_movies(arg_request):
    all_movies = TheMovie.objects.all()
    print(arg_request.GET)

    defined_movies = []
    text_for_input = arg_request.GET.get("text_for_input")
    skills = arg_request.GET.getlist('skills')
    rating_range = arg_request.GET.get("rating_range")
    release_year_from = arg_request.GET.get("release_year_from")
    release_year_to = arg_request.GET.get("release_year_to")

    for one_movie in all_movies:
        appropriate_movie = True
        # print(text_for_input)
        # print(one_movie.title)
        # print(text_for_input in one_movie.title)
        if text_for_input is not None and text_for_input != "" and text_for_input.lower() not in one_movie.title.lower():
            appropriate_movie = False
        if appropriate_movie and skills is not None:
            if type(skills) != list:
                skills = [skills]
            appropriate_movie = all(elem in list(map(lambda one_genre_name: one_genre_name.title(), list(
                one_movie.genres.all().values_list("whole_name", flat=True)))) for elem in skills)
        if rating_range is not None and rating_range != "" and not (
                float(rating_range.split()[1]) <= one_movie.movie_score <= float(rating_range.split()[3])):
            appropriate_movie = False

        if release_year_from is not None and release_year_from != "" and int(
                release_year_from) > one_movie.release_date.year:
            appropriate_movie = False

        if release_year_to is not None and release_year_to != "" and int(
                release_year_to) < one_movie.release_date.year:
            appropriate_movie = False
        if appropriate_movie:
            defined_movies.append(one_movie)
        # print(defined_movies)

    return defined_movies


# Create your views here.
def movies(request):
    defined_movies = get_appropriate_movies(request)
    all_genres = MovieGenre.objects.all()

    return render(request, 'movies/movies.html', {"defined_movies": defined_movies, "all_genres": all_genres})


def movies_list(request):
    defined_movies = get_appropriate_movies(request)
    all_genres = MovieGenre.objects.all()

    return render(request, 'movies/movies_list.html', {"defined_movies": defined_movies, "all_genres": all_genres})


def movie_single(request, movie_id):
    selected_movie = TheMovie.objects.get(pk=movie_id)
    all_stars = []
    for one_star_number in range(10):
        all_stars.append("ion-ios-star")
        if one_star_number + 1 > int(selected_movie.movie_score):
            print(int(selected_movie.movie_score))
            all_stars[-1] += "-outline"
    selected_movie_genres = []
    for one_selected_genre in selected_movie.genres.all():
        selected_movie_genres.append({"id": one_selected_genre.id, "whole_name": one_selected_genre.whole_name.title()})
    return render(request, 'movies/movie_single.html', {"selected_movie": selected_movie, "all_stars": all_stars,
                                                        "selected_movie_genres": selected_movie_genres})


def add_comment(request, movie_id):
    if request.method == 'POST':
        selected_movie = TheMovie.objects.get(pk=movie_id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')

        # comment = Comment(name=name, email=email, website=website, message=message, movie=selected_movie)
        # comment.save()

    return redirect('movie_single', movie_id=movie_id)
