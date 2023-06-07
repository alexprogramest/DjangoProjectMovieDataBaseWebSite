from django.shortcuts import render

# Create your views here.


def celebrities(request):
    return render(request, 'celebrities/celebrities.html')


def celebrities_list(request):
    return render(request, 'celebrities/celebrities_list.html')


def celebrities_single(request):
    return render(request, 'celebrities/celebrities_single.html')