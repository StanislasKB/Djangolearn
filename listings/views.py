from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Tand
from listings.models import Listing
# Create your views here.
def hello(request):
    bands=Tand.objects.all()
    return render(request,'listings/hello.html',{'bands':bands})
def contact(request):
    return HttpResponse('<h1> Page de contact</1>')

def listing(request):
    titres=Listing.objects.all()
    return render(request,'listings/listing.html',{'titre':titres} )

