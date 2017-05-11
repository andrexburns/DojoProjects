from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^complete$', views.complete),
    url(r'^register$', views.register)
    url(r'^quotes$', views.quotes),
    url(r'^add$', views.add),
    url(r'^logout$', views.logout),
    url(r'^submit$', views.submit),
    url(r'^submitreview$', views.submitreview),
    url(r'^quotes/(?P<id>\w+)$', views.showquote),
    url(r'^users/(?P<id>\w+)$', views.showuser),
    url(r'^delall$', views.delall)
]
