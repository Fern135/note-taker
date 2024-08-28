from django.shortcuts import render
from config.config import Config

def index(request):
    context = { 
        "app_name" : Config.__APP_NAME__
    }
    return render(request, 'index.html')