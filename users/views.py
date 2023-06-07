from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MovieDBUser
import random
import os


# Create your views here.

def user_registration(request):
    new_user_name = request.POST.get("username")
    new_email = request.POST.get("email")
    new_user_password = request.POST.getlist("password")
    new_user = MovieDBUser()
    new_user.nick_name = new_user_name
    new_user.password = new_user_password[0]
    new_user.email_address = new_email
    # creating the name for the directory and the directory itself
    new_user.directory_name = new_user_name + "_" + ''.join(str(random.randint(0, 9)) for _ in range(3))
    whole_path_for_folder = \
        "C:\\KPI(programming)\\6semester\\PythonWeb\\Lab1\\tortillasite\\main\\static\\main\\images\\users\\"
    os.makedirs(whole_path_for_folder + new_user.directory_name, exist_ok=True)
    new_user.save()
    # print(request.session.get("current_user_username"))
    request.session["current_user_username"] = new_user.nick_name
    request.session["current_user_directory_name"] = new_user.directory_name
    # print(request.POST)
    return redirect('main_app:home')


def user_logout(request):
    del request.session["current_user_username"]
    del request.session["current_user_directory_name"]
    # ensuring that everything is okey
    request.session.modified = True
    request.session.save()
    return redirect('main_app:home')


def user_profile(request):
    return render(request, 'users/user_profile.html')


def user_profile_password(request):
    return render(request, 'users/user_profile_password.html')


def user_favorite_grid(request):
    return render(request, 'users/user_favorite_grid.html')


def user_favorite_list(request):
    return render(request, 'users/user_favorite_list.html')
