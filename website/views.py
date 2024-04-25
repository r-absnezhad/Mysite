from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index_view(request):
    return render('<h1> This is a test </h1>')


def contact_view(request):
    return render({'name':'reihane'})

def about_view(request):
    return render({'name':'reihane'})
