from django.shortcuts import render
from django.http import HttpResponse
from landingpage.models import Email
from django.utils import timezone

# Create your views here.
def landing(request):
    #return HttpResponse("hello")
    if request.method == 'POST':
        q = Email(address=request.POST['email'], signup_date=timezone.now())
        q.save()
        return HttpResponse("Thanks for signing up!")
    else:
        return render(request, 'landingpage/landing.html')
    #return render(request, 'landingpage/landing.html')