from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm
from django.contrib.auth.models import User


def home(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    context = {
        'treasures': treasures,
        'form': form,
    }
    return render(request, 'home.html', context)


def detail(request, treasure_id):
    treasure = Treasure.objects.get(pk=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})


def post_treasure(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        treasure = form.save(commit=False)
        treasure.user = request.user
        treasure.save()
    return HttpResponseRedirect('/')


def profile(request, username):
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    return render(request, 'profile.html',
                  {'username': username,
                   'treasures': treasures})
