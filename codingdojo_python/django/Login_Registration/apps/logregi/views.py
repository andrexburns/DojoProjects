from django.shortcuts import render, redirect
from .models import Registration
from django.contrib import messages
def index(request):
    # Registration.objects.all().delete()
    info = Registration.objects.all()
    context = {
    'infos' : info
    }
    return render(request, 'logregi/index.html', context)

def registration(request):
    if request.method == "POST":
        validated_person = Registration.objects.register(request.POST)
        if 'errors' in validated_person:
            for validation_error in validated_person['errors']:
                messages.error(request, validation_error)
        if 'the_person' in validated_person:
            messages.success(request, 'registered successfully!')
        email = request.POST['email']

    return redirect('/')

def login(request):
    # user = request.POST['log_email']
    # userpw = request.POST['log_pw']
    # username = Registration.objects.all()
    # if Registration.objects.filter(email= user):
    #     if Registration.objects.filter(password = userpw):
    #         context = {'username' : username }
    #         return render(request, 'logregi/success.html', context)
    if request.method =="POST":
        user = Login.objects.login(request.POST)
        if 'errors' in user:
            for login_error in user['errors']:
                messages.error(request, validation_error)
        if ''
    return redirect('/')
# Create your views here.
