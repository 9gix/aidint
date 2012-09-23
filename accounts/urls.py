from django.conf.urls import patterns, include, url


urlpatterns = patterns('accounts.views',
    url(r'^', include('registration.backends.default.urls')),
)
