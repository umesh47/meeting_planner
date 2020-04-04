from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")



def date(request):
    return HttpResponse("This page was served at "+ str(datetime.now()))

# Please add: An about page that shows some text about yourself

def about(request):
    return HttpResponse("hello, I am umesh. I am from Nepal.")