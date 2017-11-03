from django.shortcuts import render


def home(request):
	#The Class Treasure will have a
	class Treasure:
		#constructor that sets all of its attributes.
		def __init__(self, name, value, material, location):
			self.name = name
			self.value = value
			self.material = material
			self.location = location
			
	#Then we can create a treasure object and set its attributes with one line of code
	t1 = Treasure('Gold Nugget', 500.00, 'gold', "Curl's Creek, NM")
	t2 = Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO")
	t3 = Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA')
	#This creates three Treasures, each with its own values (or instance variables)

	return render(request, 'home.html', context)
