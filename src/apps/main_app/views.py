from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Treasure
from .forms import TreasureForm, LoginForm
from django.contrib.auth import authenticate, login, logout
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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print('The account has been disabled!')
            else:
                print('The username and password were incorrect.')
    else:
        form = LoginForm()
        return render(request, 'login.html',
                      {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def like_treasure(request):
    treasure_id = request.POST.get('treasure_id', None)

    likes = 0
    if (treasure_id):
        treasure = Treasure.objects.get(id=int(treasure_id))
        if treasure is not None:
            likes = treasure.likes + 1
            treasure.likes = likes
            treasure.save()
    return HttpResponse(likes)
