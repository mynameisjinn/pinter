from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def hello_world(request):
    return render(request, 'base.html')