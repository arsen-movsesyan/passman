from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^acct/*', include('passman.urls')),
    url(r'^vehicle/*', include('vehicle.urls')),
    url(r'^people/*', include('people.urls')),

#    url(r'^admin/', include(admin.site.urls)),
]
