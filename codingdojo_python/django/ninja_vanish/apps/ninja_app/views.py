from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context={
        "turtle":"none"
    }
    print context
    return render(request, 'ninja_app/index.html', context)

def ninjas(request):
    context={
        "turtle":"ninjas"
    }
    print context
    return render(request, 'ninja_app/index.html', context)

def ninjacolor(request, color):
    context={
        "turtle":color
    }
    print context
    return render(request, 'ninja_app/index.html', context)
