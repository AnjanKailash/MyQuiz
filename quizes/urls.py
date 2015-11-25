#user created file - in apps -- in Project folder it is present by default 
from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /quizes/
    url(r'^$', views.index, name='index'),
    # ex: /quizes/5/
    url(r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /quizes/5/results/
    url(r'^(?P<quiz_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /quizes/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.submit, name='submit'),
]
  