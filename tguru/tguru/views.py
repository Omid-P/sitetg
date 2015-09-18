__author__ = 'alexhooker'
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def landing(request):
    #return HttpResponse("hello")
    return render(request, 'landingpage/landing.html')
    #return render(request, 'landingpage/landing.html')