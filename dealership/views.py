from django.http import HttpResponse
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Car
# Create your views here.
def indexPageView(request) :

    cars = Car.objects.all()
    context = {
        'cars' : cars,
    }
    return render(request, 'dealership/index.html', context) 

def aboutPageView(request) :
    return render(request, 'dealership/about.html') 

def contactPageView(request) :
    return render(request, 'dealership/contact.html') 

def createPageView(request) :
    if request.method == 'POST' :
        
        newCar = Car()

        newCar.make = request.POST['make']
        newCar.model = request.POST['model']
        newCar.year = request.POST['year']
        newCar.color = request.POST['color']
        newCar.mileage = request.POST['mileage']
        if request.POST['clean_title'] == "True":
            newCar.cleanTitle = True
        else:
            newCar.cleanTitle = False

        newCar.save()
        return redirect('index')

    else:
        return render(request, 'dealership/create.html')

def showSingleEntryPageView(request, car_id) :
    data = Car.objects.get(id = car_id)

    context = {
        "record" : data,
    }
    return render(request, 'dealership/update.html' , context)

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