from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm


def home(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    context = {
        'form': form,
        'treasures': treasures,
    }
    return render(request, 'home.html', context)


def detail(request, treasure_id):
    treasure = Treasure.objects.get(pk=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})


def post_treasure(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        form.save(commit = True)
    treasure.save()

    return HttpResponseRedirect('/')

