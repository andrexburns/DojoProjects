from django.shortcuts import render, redirect, reverse
from .models import user,author, quote, review
from datetime import datetime
from django.contrib import messages
from django.db.models import count


# Create your views here.
def index(request):
    print user.objects.all()
    return render(request, "b_exam/index.html")

def register(request):
    register = user.objects.register(request.POST['first_name'], request.POST['last_name'],request.POST['dob'],request.POST['email'],request.POST['password'],request.POST['password2'])
    if datetime.strptime(request.POST['dob'], '%Y-%m-%d')>datetime.now():
        print "TOP"
    else:
        print "BOTTOM"
    if register[0] == True:
        messages.info(request, register[1])
        return redirect('/complete')
    else:
        messages.error(request, register[1])
        return redirect('/')
def complete(request):
    return render(request, 'b_exam/complete.html')
def login(request):
    login = user.objects.login(request.POST['email'], request.POST['password'])
    if login[0] == true:
        messages.info(request, login[1])
        return redirect('/complete')
    else:
        messages.error(request, login[1])
        return redirect('/')
def quotes(request):
    if "user" not in request.session:
    messages.info(request, "User not logged in")
    return redirect('/')
else:
    context={
        "reviews":Review.objects.all().order_by('-created_at')[:3],
        "quotes":quotes.objects.all()
    }
    return render(request,'b_exam/quotes.html', context)

def add(request):
    if "user" not in request.session:
        messages.info(request, "User not logged in")
        return redirect('/')
    else:
        context={
            "authors":Author.objects.all()
        }
        return render(request,'b_exam/add.html', context)
def logout(request):
    request.session.pop('user')
    return redirect('/')
def submit(request):
    if "user" not in request.session:
        messages.info(request, "User not logged in")
        return redirect('/')
    else:
        this_user=User.objects.get(email=request.session['user'])
        # author=request.POST['author']
        # author2=request.POST['author2']
        # if not author:
        #     print "author 1 NONE"
        # if not author2:
        #     print "author 2 NONE"
        if len(request.POST['quote2'])>1:
            author=request.POST['quote2']
        else:
            author=request.POST['quote']
        if Author.objects.filter(name=quote).exists():    # add new author if no author name exists
            this_author=Author.objects.get(name=quote)
        else:
            Author.objects.create(name=author)
            this_author=Author.objects.get(name=quote)
        if quotes.objects.filter(title=request.POST['title']).exists():
            this_quotes=quotes.objects.get(title=request.POST['title'])
        else:
            quotes.objects.create(title=request.POST['title'],quote_id=this_author.id)
            this_quote=quote.objects.get(title=request.POST['title'])
        Review.objects.create(review=request.POST['review'],rating=request.POST['rating'],quote_id=this_quote.id,user_id=this_user.id)
        authors = Author.objects.all()
        return redirect('/quotes')
def submitreview(request):
    if "user" not in request.session:
        messages.info(request, "User not logged in")
        return redirect('/')
    else:
        this_user=User.objects.get(email=request.session['user'])
        this_quote=quote.objects.get(id=request.POST['id'])
        Review.objects.create(review=request.POST['review'],rating=request.POST['rating'],quote_id=this_quote.id,user_id=this_user.id)
        return redirect('/quotes')

def showquote(request, id):
    if "user" not in request.session:
        messages.info(request, "User not logged in")
        return redirect('/')
    else:
        context={
            "quote":quote.objects.get(id=id),
            "reviews":Review.objects.filter(quote_id=id)
        }
        return render(request,'b_exam/showquote.html', context)

def showuser(request, id):
    if "user" not in request.session:
        messages.info(request, "User not logged in")
        return redirect('/')
    else:
        context={
            "user":User.objects.annotate(num_reviews=Count('userreviews')).get(id=id),
            "reviews":Review.objects.filter(user_id=id)
        }
        return render(request,'b_exam/showuser.html', context)

def delall(request):
    if "user" not in request.session:
        messages.info(request, "User not logged in")
        return redirect('/')
    else:
        Author.objects.all().delete()
        quote.objects.all().delete()
        Review.objects.all().delete()
        print "EVERYTHING EXCEPT USER TABLE DELETED"
        return redirect('/')
