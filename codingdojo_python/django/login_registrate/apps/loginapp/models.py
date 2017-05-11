from __future__ import unicode_literals
import re
import bcrypt


from django.db import models
class UserManager(models.Manager):
    def register(self,request,post_data):
        Emsg = []
        emailregx = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        fnameregx  = re.compile(r'^[a-zA-Z]\w+$')
        lnameregx = re.compile(r'^[a-zA-Z]\w+$')
        if post_data['email'] <0:
            Emsg.append('Emails')
        if not emailregx.match(post_data['email']):
            Emsg.append('seems your not registered. try again?')
        if not fnameregx.match(post_data['first_name']):
            Emsg.append('invalid first name, try again.')
        if not lnameregx.match(post_data['last_name']):
            Emsg.append('invalid last name, please try again')
        if len(post_data['first_name']) < 2:
            Emsg.append('first name too short, try again')
        if len(post_data['last_name']) < 2:
            Emsg.append('last name too short, try again')
        if len(post_data['password']) < 8:
            Emsg.append('too short of a password, try again')
        if not post_data['password'] == post_data['confirm_password']:
            Emsg.append('invalid password, are u the user????')
        if Emsg:
            return{
                'errors': Emsg
            }
        else:
            new_user = User.objects.create(
            First_name = post_data['first_name'],
            Last_name = post_data['last_name'],
            email=post_data['email'],
            Password=post_data['password'],
            Confirm=post_data['confirm_password'])
            bcrypt_password = post_data['confirm_password'].encode('UTF_8'), bcrypt.gensalt())
            return {
            'the_user' : user.
            }
        pass
    def login(self, post_data):
        print "this is the post data"
        A_user = user.objects.filter(email = post_data['email'].encode(UTF_8))
        Emsg = []
        emailregx = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not emailregx.match(post_data['email']):
            Emsg.append('email not valid, try again')
        if not post_data['email'] == User.objects.get(Email = post_data['email']):
            Emsg.append('email does not match our records')
        if Emsg:
            return{
                'errors' : Emsg
            }
        else:
            return 'the_user'

class User(models.Model):
      First_name = models.CharField(max_length=45)
      Last_name = models.CharField(max_length=45)
      Password = models.CharField(max_length=100)
      Email = models.CharField(max_length = 45)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = UserManager()

# Create your models here.
