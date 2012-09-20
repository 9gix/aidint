from django.conf.urls import patterns, include, url


urlpatterns = patterns('project.views',
    url(r'^(?P<project_id>\d+)/$', 'project_detail', name='project-detail'),
    url(r'^$', 'index'),
)
