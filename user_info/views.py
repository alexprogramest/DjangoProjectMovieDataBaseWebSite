from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def one_user_info_page(request, personal_user_id):
    return HttpResponse(f"<h3>Сторінка інформації про користувача, який має ID: {personal_user_id}</h3>")
