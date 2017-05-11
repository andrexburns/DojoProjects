from django.shortcuts import render
import random
import string
# Create your views here.
def index(request):
    if 'string' not in request.session:
        request.session['string'] =''
    return render(request, 'first_app/index.html')
def create(request):
    request.session['string'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
    context = {
        'string' : request.session['string']
    }

    #generate random number
    return render(request, 'first_app/index.html', context)
