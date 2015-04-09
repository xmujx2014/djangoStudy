from django.conf.urls import patterns, url

import views

urlpatterns = [
    url(r'^$', views.teaminfo, name='teaminfo'),
    url(r'^addPerson/?$', views.addPerson, name='addPerson'),
    ]