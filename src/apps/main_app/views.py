from django.shortcuts import render
from .models import Treasure


def home(request):
    treasures = Treasure.objects.all()
    return render(request, 'home.html', {'treasures': treasures})


def detail(request, treasure_id):
    treasure = Treasure.objects.get(pk=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})
