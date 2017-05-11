from django.shortcuts import render, HttpResponse, redirect
def new_user(request):
    # for /new_user in index:
    #     index.sessions = "/new_user",
    #     if
    #     return redirect('/new_user.sessions')
    pass
def create(request):
    print "Hit the create method"
    print request.session
    print request.POST
    request.session['survey_name'] = request.POST['full_name']
    request.session['survey_locate'] = request.POST['dojo_location']
    request.session['survey_lang'] = request.POST['favorite_language']
    request.session['survey_comment'] = request.POST['comment']
    print request.session['survey_name']
    return redirect('/formview')
def index(request):
    print "Hit the index method"
    return render(request, 'survey_form/index.html')
def survey(request):
    return render(request, "survey_form/index2.html")
