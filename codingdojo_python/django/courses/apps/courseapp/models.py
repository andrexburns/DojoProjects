from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Course(models.Model):
      Title = models.CharField(max_length=45)
      description = models.TextField(max_length=1000)
      # Notice the association made with ForeignKey for a one-to-many relationshi
      created_at = models.DateTimeField(auto_now_add = True)
