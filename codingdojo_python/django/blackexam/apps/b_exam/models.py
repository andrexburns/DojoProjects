from __future__ import unicode_literals
from datetime import datetime
import bcrypt
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^\d.*[A-Z]|[A-Z].*\d')
from django.db import models

class usermanager(models.Manager):
    def register(self, first_name, last_name, dob, email, password, password2):
        if len(first_name) <2 or len(last_name) <2 or len(email) <1 or len(password)<1:
            return(False, "all fields required")
        elif not (NAME_REGEX.match(first_name) and NAME_REGEX.match(last_name)):
            return (False, "error!invalid name")
        elif datetime.strptime(dob,'%Y-%m-%d')>datetime.now():
            return (False, "error! invalid dob")
        elif not EMAIL_REGEX.match(email):
            return (False, "error! invalid email")
        elif not PASS_REGEX.match(password):
            return (False, "error! invalid password")
        else:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            print hashed
            user.objects.create(first_name=first_name, last_name=last_name, dob=dob, email=email, pwhash=hashed)
            string = "registration complete! welcome " + first_name + " ! "
            return (True,string)
        def login(self, email, password):
            if len(email) <1 or len(password) <1:
                return (False, "requirments noy yet completed")
            elif not EMAIL_REGEX.match(email):
                return (False, "requirments not yet completed")
            else:
                try:
                    user = user.objects.get(email = email)
                except:
                    return (False, "email address unknown")
                else:
                    if bcrypt.hashpw(password.encode('utf-8'), user.pwhash.encode('utf-8')) == user.pwhash:
                        string = "you logged in! welcome" + user.first_name + "!"
                        return (True, string)
                    else:
                        return (False, "invalid password")
class user(models.Model):
    first_name=models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    pwhash = models.CharField(max_length = 255)
    dob = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = usermanager()
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + str(self.dob)

class quote(models.Model):
    title = models.CharField(max_length = 100)
    quote = models.foreign(quotes, related_name = "quote")
    created_at = models.DateTimeField(auto_now_add = true)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.quote

class review_quote(models.Model):
    review = models.TextField()
    quote = models.Foreighnkey(quote, related_name)

class quote(models.Model):
    title=models.CharField(max_length=100)
    quote=models.ForeignKey(Author, related_name="quotes")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Review(models.Model):
    review=models.TextField()
    rating=models.IntegerField()
    quote=models.ForeignKey(quote, related_name="quotereviews")
    user=models.ForeignKey(User, related_name="userreviews")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Author(models.Model):
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name





# Create your models here.
