from django.shortcuts import render, redirect
from .models import Course
from datetime import datetime
from .models import *

def  index(request):
    context = {
        "courses": Course.objects.all(),
        "undo": Course.objects.all().delete()
    }
    return render(request, 'courseapp/index.html', context)

def create(request):
    if request.method == "POST":
        Course.objects.create(Title = request.POST['titleadd'])
        Course.objects.create( description = request.POST['describe'])

    return redirect('/')

def remove(request):
    if request.POST.get('delete'):
        Course.objects.all().delete(Title = request.Post["titlermv"]).delete(description = request.POST["describermv"])

    return redirect('/')
