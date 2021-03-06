from django.conf.urls.defaults import *

from socialite.apps.facebook import views

urlpatterns = patterns('',
    url(r'^authenticate/$', views.authenticate, name='facebook_authenticate'),
    url(r'^authorize/$', views.authorize, name='facebook_authorize'),
    url(r'^callback/$', views.mediator.callback, name='facebook_callback'),
    url(r'^canvas/$', views.canvas, name='facebook_canvas'),
)
