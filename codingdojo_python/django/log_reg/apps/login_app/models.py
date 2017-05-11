from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def validate_reg(self, post_data):
        Emasg = []
        if len(post_data['email']) < 1:
            Emsg.append("no no")
        if post_data['password'] != post_data['c_pass']:
            Emsg.append("pdm")
        if Emsg:
            return{ 'errors': Emsg}
        else:
            return {'the_user': none}
        pass

    def validate_login(self, post_data):
        pass

class User(models.Model):
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 60)
    objects = UserManager
# Create your models here.
