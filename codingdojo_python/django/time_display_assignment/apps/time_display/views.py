from django.shortcuts import render, redirect
#CONTROLLER!!!!
# Create your views here.
import datetime
def index(request):
    context = {
        'time':datetime.datetime.now(),

    }

    return render(request, "time_display/index.html", context)
