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


def user_login(request):
    print(request.POST)
    login_user_name = request.POST.get("username")
    login_user_password = request.POST.get("password")
    # print(MovieDBUser.objects.all()[0])
    all_usernames = MovieDBUser.objects.all().values_list('nick_name', flat=True)
    # print(all_usernames)
    if login_user_name in all_usernames:
        print("user exists!")
        # print(MovieDBUser.objects.get(nick_name=login_user_name))
        current_user = MovieDBUser.objects.get(nick_name=login_user_name)
        if login_user_password == current_user.password:
            request.session["current_user_username"] = current_user.nick_name
            request.session["current_user_directory_name"] = current_user.directory_name
        else:
            request.session["login_error"] = "incorrect password"
    else:
        request.session["login_error"] = "incorrect username"
        print("user doesn't exists!")
    return redirect('main_app:home')


def user_logout(request):
    del request.session["current_user_username"]
    del request.session["current_user_directory_name"]
    # ensuring that everything is okey
    request.session.modified = True
    request.session.save()
    return redirect('main_app:home')


def user_profile(request):
    current_user_name = request.session.get("current_user_username")

    if current_user_name:
        current_user = MovieDBUser.objects.get(nick_name=current_user_name)
        if request.method == "POST":
            print(request.POST)
            change_nick_name = request.POST.get("change_nick_name")
            change_email_address = request.POST.get("change_email_address")
            change_first_name = request.POST.get("change_first_name")
            change_last_name = request.POST.get("change_last_name")
            change_country = request.POST.get("change_country")
            change_state = request.POST.get("change_state")

            if change_nick_name != "":
                current_user.nick_name = change_nick_name
            if change_email_address != "":
                current_user.email_address = change_email_address
            if change_first_name != "":
                request.session["current_user_first_name"] = current_user.first_name = change_first_name
            if change_last_name != "":
                request.session["current_user_last_name"] = current_user.last_name = change_last_name
            if change_country != "":
                current_user.country = change_country
            if change_state != "":
                current_user.state = change_state
            current_user.save()

            request.session["current_user_username"] = current_user.nick_name
            request.session["current_user_directory_name"] = current_user.directory_name

        user_profile_info = {"current_user": current_user}
    else:
        return redirect('main_app:home')
    return render(request, 'users/user_profile.html', user_profile_info)


def user_profile_password(request):
    current_user_name = request.session.get("current_user_username")

    if current_user_name:
        current_user = MovieDBUser.objects.get(nick_name=current_user_name)
        if request.method == "POST":
            print(request.POST)
            current_user_old_password = request.POST.get("old_password")
            current_user_new_password1 = request.POST.get("new_password1")
            current_user_new_password2 = request.POST.get("new_password2")

            current_user.password = current_user_new_password1
            current_user.save()
        user_profile_info = {"current_user": current_user}
    else:
        return redirect('main_app:home')
    return render(request, 'users/user_profile_password.html', user_profile_info)


def user_favorite_grid(request):
    return render(request, 'users/user_favorite_grid.html')


def user_favorite_list(request):
    return render(request, 'users/user_favorite_list.html')
