from django.conf.urls import patterns, include, url

from passman import views



urlpatterns = patterns('',

    url(r'^$', views.accounts,{'in_acct_iden':'active'}),
    url(r'^all$', views.accounts,{'in_acct_iden':'all'}),
#    url(r'^payments$', views.accounts,{'in_acct_iden':'payments'}),
    url(r'^payments$', views.payments),

    url(r'^(?P<in_acct_id>\d+)$', views.single_account),
    url(r'^acknowledge/(?P<in_acct_id>\d+)$', views.acknowledge),
    url(r'^payment_history/(?P<in_acct_id>\d+)$', views.payment_history),
    url(r'^edit_account/(?P<in_acct_id>\d+)$', views.edit_account),
    url(r'^acct_attributes/(?P<in_acct_id>\d+)$', views.add_edit_account_attributes),
    url(r'^acct_attributes/account/(?P<in_acct_id>\d+)/remove_attr/(?P<in_attr_id>\d+)$', views.remove_acct_attribute),
    url(r'^manage_categories$', views.manage_categories),
    url(r'^manage_categories/remove/(?P<in_cat_id>\d+)$', views.remove_category),
    url(r'^manage_attributes$', views.manage_attributes),
    url(r'^manage_attributes/remove/(?P<in_attr_id>\d+)$', views.remove_attribute),
    url(r'^add_account$', views.add_account),
)
