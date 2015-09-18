__author__ = 'alexhooker'
from django.shortcuts import render
from django.http import HttpResponse
def landing(request):
    return HttpResponse("hello")
    #return render(request, '../landing.html')