from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	name = 'Gold Nugget'
	value = 1000.00
	context = {
		'treasure_name': name,
		'treasure_value': value,
	}

	return render(request, 'home.html', context)
