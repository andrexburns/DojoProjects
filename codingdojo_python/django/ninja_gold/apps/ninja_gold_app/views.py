from django.shortcuts import render, HttpResponse, redirect
import datetime
import random
def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    if "log" not in request.session:
        request.session['log'] = []
    return render(request, "ninja_gold_app/index.html")
    # for /new_user in index:
    #     index.sessions = "/",
    #     if
    #     return redirect('/new_user.sessions')
    pass
def process(request):
    if request.method == 'POST':
        request.session['action'] = request.POST['action']
        if request.session['action'] == 'farm':
            diff = randomize(10,20)
            request.session['gold'] += diff
            request.session["log"].insert(0, "earned " + str(diff) + " gold from farm"  + str(datetime.datetime.now()).split('.')[0])
        elif request.session['action'] == 'cave':
            diff = randomize(5, 10)
            request.session['gold'] += diff
            request.session["log"].insert(0, "earned " + str(diff) + " gold from cave" + str(datetime.datetime.now()).split('.')[0])
        elif request.session['action']  == 'house':
            diff = randomize(2, 5)
            request.session['gold'] += diff
            request.session["log"].insert(0, " earned " + str(diff) + " gold from house " + str(datetime.datetime.now()).split('.')[0])
        elif request.session['action'] == 'casino':
            if randomize(0, 1):
                diff = randomize(0, 50)
                request.session['gold'] += diff
                request.session["log"].insert(0, "earned " + str(diff) + " gold at casino " + str(datetime.datetime.now()).split('.')[0])
            else:
                diff = randomize(0, 50)
                request.session['gold'] -= diff
                request.session["log"].insert(0, "lost " + str(diff) + "gold at casino" + str(datetime.datetime.now()).split('.')[0])
        return redirect('/')

def randomize(start,end):
    return random.randint(start,end)
