from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from http.client import HTTPResponse
# Create your views here.
def indexPageView(request) :
    return HttpResponse('This is our homepage')

def aboutPageView(request) :
    return HttpResponse('This is our about page')

def contactPageView(request) :
    return HttpResponse('This is our contact page')