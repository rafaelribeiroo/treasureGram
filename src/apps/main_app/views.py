from django.shortcuts import render

#The Class Treasure will have a
class Treasure:
	#constructor that sets all of its attributes.
	def __init__(self, name, value, material, location, img_url):
		self.name = name
		self.value = value
		self.material = material
		self.location = location
		self.img_url = img_url

treasures = [
	Treasure('Gold Nugget', 500.00, 'gold', "Curl's Creek, NM", 'https://images4.sw-cdn.net/product/picture/710x528_712638_576979_1459314196.jpg'),
	Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO", 'https://sep.yimg.com/ay/yhst-135466925550166/7-45-gram-australia-gold-nugget-5.gif'),
	Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA', 'https://factorydirectcraft.com/factorydirectcraft_blog/wp-content/uploads/2011/07/Coffee_Can_Bird_Feeder2.jpg'),
]

def home(request):
	return render(request, 'home.html', {'treasures':treasures})
