from django.conf.urls import patterns, include, url

from people import views



urlpatterns = patterns('',

    url(r'^person/$', views.person),
    url(r'^address/$', views.address_history),

)
