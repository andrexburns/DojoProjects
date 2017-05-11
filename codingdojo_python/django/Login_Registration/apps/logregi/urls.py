from django.conf.urls import url, include
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^regi$', views.registration),
    url(r'^login$', views.login),
]
