from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout


urlpatterns = patterns('accounts.views',
    url(r'^logout/$',logout, {'next_page':'/'}),
    url(r'^', include('registration.backends.default.urls')),
)
