from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register(self, postdata):
        errormsg = []
        emailregex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        nameregex = re.compile(r'^[a-zA-Z]\w+$')
        if postdata['email'] < 0:
            errormsg.append('emails')
        if not emailregex.match(postdata['email']):
            errormsg.append('not validated lol')
        if not nameregex.match(postdata['name']):
            errormsg.append('your first name contains number')
        if len(postdata['name']) < 2:
            errormsg.append('first name is too short')
        if len(postdata['password']) < 8:
            errormsg.append('make it more than 8 characters')
        if not postdata['password'] == postdata['confirm']:
            errormsg.append('password does not match')
        if errormsg:
            return{
            'errors': errormsg
            }
        else:
            created_person = Registration.objects.create(
            name=postdata['name'],
            email=postdata['email'],
            password=postdata['password'],
            confirm=postdata['confirm'])
            bcrypt_password = postdata['password'].encode()
            hashed = bcrypt.hashpw(bcrypt_password, bcrypt.gensalt())
            return {
            'the_person' : created_person
            }
    def login(self, postdata):
        errormsg = []
        emailregex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not emailregex.match(postdata['email']):
            errormsg.append('not validated lol')
        if not postdata['email'] == Registration.objects.get(email=postdata['email']):
            errormsg.append('wtf')
        if errormsg:
            return{
            'errors' : errormsg
            }
        else:
            errormsg.append('gj')
class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    confirm = models.CharField(max_length=30)
    objects = UserManager()
# Create your models here.
