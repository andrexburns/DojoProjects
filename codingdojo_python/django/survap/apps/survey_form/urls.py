from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_user$', views.create),
    url(r'^formview$', views.survey)
]
# In flask:
# @app.route('/')
# def homepage():
#   return render_template('index.html')

# In django:
# in urls.py:
# url(r'^$', views.homepage)
#  |
#  V
# in views.py:
# def homepage(request):
#   return render(request, 'survey_form/index.html')
