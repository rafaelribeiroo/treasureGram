from django.shortcuts import render

#The Class Treasure will have a
class Treasure:
	#constructor that sets all of its attributes.
	def __init__(self, name, value, material, location):
		self.name = name
		self.value = value
		self.material = material
		self.location = location

treasures = [
	Treasure('Gold Nugget', 500.00, 'gold', "Curl's Creek, NM"),
	Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
	Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA'),
]

def home(request):
	return render(request, 'home.html', {'treasures':treasures})
