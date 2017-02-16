from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#homepage view.
#to learn how to create views with render.
def index(request):
    return HttpResponse("Hello from polls.")
