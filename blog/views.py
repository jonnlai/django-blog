from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def message(response):
    return HttpResponse("Hello, Blog!")
