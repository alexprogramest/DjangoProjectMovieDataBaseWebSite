from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def user_registration(request):
    return HttpResponse("<h3>Реєстрація користувача...</h3>")


def user_authorization(request):
    return HttpResponse("<h3>Авторизація користувача...</h3>")
