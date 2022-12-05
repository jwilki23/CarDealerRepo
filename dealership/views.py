from django.http import HttpResponse
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Car
# Create your views here.
def indexPageView(request) :
    return render(request, 'dealership/index.html') 

def aboutPageView(request) :
    return render(request, 'dealership/about.html') 

def contactPageView(request) :
    return render(request, 'dealership/contact.html') 

def createPageView(request) :
    if request.method == 'POST' :
        
        newCar = Car()

        Car.make = request.POST['make']
        Car.model = request.POST['model']
        Car.year = request.POST['year']
        Car.color = request.POST['color']
        Car.mileage = request.POST['mileage']
        if request.POST['clean_title'] == "True":
            Car.cleanTitle = True
        else:
            Car.cleanTitle = False

        Car.save()
        return redirect('index')

    else:
        return render(request, 'dealership/create.html')

def updatePageView(request) :

    if request.method == 'POST' :
        car_id = request.POST['car_id']

        car = Car.objects.get(id=car_id)
    
        car.make = request.POST['make']
        car.model = request.POST['model']
        car.year = request.POST['year']
        car.color = request.POST['color']
        car.mileage = request.POST['mileage']
        if request.POST['clean_title'] == "True":
            car.cleanTitle = True
        else:
            car.cleanTitle = False

        car.save()
    return redirect('index')

def deletePageView(request, car_id) :

    data = Car.objects.get(id = car_id)

    data.delete()

    return indexPageView(request)