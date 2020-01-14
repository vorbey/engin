from django.shortcuts import render
import requests

def index(request):
    return render(request,('gop/index.html'))
# Create your views here.
