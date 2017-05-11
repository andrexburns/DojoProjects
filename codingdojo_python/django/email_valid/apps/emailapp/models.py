from __future__ import unicode_literals

from django.db import models
class UserManager(models.Manager):
      def login(self, postData):
        email = postData['email']
        if email != "test@test.com":
            return {'error:' "wrong email"}
        else:
            return {'email':email}
class User(models.Model):
      email = models.CharField(max_length=45)
      # *************************
      # Connect an instance of UserManager to our User model overwriting
      # the old hidden objects key with a new one with extra properties!!!
      objects = UserManager()
      # *************************
      # Notice the association made with ForeignKey for a one-to-many relationshi
