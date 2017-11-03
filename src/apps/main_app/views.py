from django.shortcuts import render


def home(request):
    name = 'Gold Nugget'
    value = 1000.00
    context = {
        'treasure_name': name,
        'treasure_value': value,
    }

    return render(request, 'home.html', context)
