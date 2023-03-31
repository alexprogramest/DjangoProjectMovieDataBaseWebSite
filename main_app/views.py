from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_page(request):
    return HttpResponse("<h2>Головна сторінка</h2>")


def about_page(request):
    return HttpResponse("<h3>Інформаційна сторінка 'Про нас'</h3>")
