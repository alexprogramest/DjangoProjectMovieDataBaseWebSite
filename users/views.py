from django.shortcuts import render

# Create your views here.


def user_profile(request):
    return render(request, 'users/user_profile.html')


def user_profile_password(request):
    return render(request, 'users/user_profile_password.html')


def user_favorite_grid(request):
    return render(request, 'users/user_favorite_grid.html')


def user_favorite_list(request):
    return render(request, 'users/user_favorite_list.html')