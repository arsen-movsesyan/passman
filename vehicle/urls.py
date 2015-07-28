from django.conf.urls import patterns, include, url

from vehicle import views



urlpatterns = patterns('',

#    url(r'^$', views.car),
    url(r'^$', views.issue_date_lookup),
    url(r'^add_vehicle$', views.add_vehicle),
    url(r'^all_vehicles$', views.see_all_vehicles),
    url(r'^renew_vehicle$', views.renew_from_menu),
    url(r'^edit/(?P<in_vehicle_id>\d+)$', views.vehicle_edit),
    url(r'^renew/(?P<in_vehicle_id>\d+)$', views.vehicle_renew),

)