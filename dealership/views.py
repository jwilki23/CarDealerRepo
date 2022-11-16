from django.http import HttpResponse
from http.client import HTTPResponse
from django.shortcuts import render
# Create your views here.
def indexPageView(request) :
    return render(request, 'dealership/index.html') 

def aboutPageView(request) :
    return render(request, 'dealership/about.html') 

def contactPageView(request) :
    return render(request, 'dealership/contact.html') 