from django.shortcuts import render
from django.http import httpResponse

def index(request):
    return httpResponse("Seja bem-Vindo")


# Create your views here.
