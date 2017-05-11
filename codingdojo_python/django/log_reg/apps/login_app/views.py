from django.shortcuts import render
from django.contrib import messages
from models import User
import bcrypt
import re

def home(request):
    return render(request,'login_app/index.html')
def register(request):
    if request.method == "POST":
        print request.POST
        the_user = User.objects.validate_reg(request.POST)
        if errors in thing:
            print thing['errors']
        for error in thing['errors']:
            print error
            messages.error(request, error)
    return redirect('/')
