from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    context = {
    }
    return render(request, 'loginapp/index.html')


def register(request):
    if request.method == "POST":
        users = User.objects.validate_reg(request.POST)
        if 'errors' in new_user['success']:
            messages.success(request, success)
        email = request.POST['email']

    return redirect('/')
def login(request):
    if request.method == "POST":
        Login = register.objects.validate_login(request.POST)
    for Login in login['email', 'password']:
        new_user = User.objects.login(request.POST)
    if new_user == User.request.login(post_data['email'], post_data['password']):
#messages.errors#
        pass

        return messages.success(request, success)
        return redirect('/loginapp/index2.html')
