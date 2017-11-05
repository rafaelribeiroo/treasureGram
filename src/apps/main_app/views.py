from django.shortcuts import render
from .models import Treasure


def home(request): 
    treasures = Treasure.objects.all()
    return render(request, 'home.html', {'treasures':treasures})
