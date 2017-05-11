from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/course$', views.create),
    url(r'^delete$', views.delete)
]
