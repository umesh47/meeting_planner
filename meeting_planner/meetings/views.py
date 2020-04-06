from django.shortcuts import render, get_object_or_404
from .models import Meeting,Room

def detail(request,id):
    meeting= get_object_or_404(Meeting, pk=id)
    return render(request,'meetings/detail.html',{'meeting':meeting})

#Please add a new page that shows a list of all room objects
# (just text, no links)

#create a 
# view
# template
# url mapping


def rooms_list(request):
    return render(request, 'meetings/rooms_list.html',{'rooms':Room.objects.all()})