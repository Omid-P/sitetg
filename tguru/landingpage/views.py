from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    #return HttpResponse("hello")
    if request.method == 'POST':
        return HttpResponse("Thanks for signing up!")
    else:
        return render(request, 'landingpage/landing.html')
    #return render(request, 'landingpage/landing.html')