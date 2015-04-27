from django.conf.urls import patterns, url
from drirfinder import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^display/$', views.display, name='display'))