from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return render(request, "website/welcome.html",{"message": "THis data was sent from views","x":"demo from views"})


def date(request):
    return HttpResponse("This page was served at "+ str(datetime.now()))

# Please add: An about page that shows some text about yourself

def about(request):
    return HttpResponse("hello, I am umesh. I am from Nepal.")