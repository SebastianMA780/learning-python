from django.shortcuts import render

# Create your views here.
def car_view(request):
		car_list = [
				{'name': 'Audi', 'description': 'Audi is good car'},
				{'name': 'BMW', 'description': 'BMW is good car'},
				{'name': 'Mercedes', 'description': 'Mercedes is good car'},
		]
		context = {
				'car_list': car_list
		}
		return render(request, 'first_example/car_list.html',context)