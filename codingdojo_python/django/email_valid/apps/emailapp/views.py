from django.shortcuts import render, redirect, HttpResponse
from .models import User
# Create your views here.
def index(request):
    context = {
        "email_val": User.objects.all()
    }

def users(request):
    if request.method == "POST":
        User.objects.create(email = request.POST["email_log"])
        return redirect('/')

        #print("Running index method, calling out to User.")
      user = User.objects.login()
# DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
      print (type(user))
      if 'error' in user:
          pass
      if 'theuser' in user:
          pass
      return HttpResponse("Done running userManager method. Check your terminal console.")
