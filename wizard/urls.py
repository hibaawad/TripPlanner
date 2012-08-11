from django.conf.urls import patterns, include, url

urlpatterns = patterns('wizard.views',
    url(r'^$', 'home'),
    url(r'^(?P<city>\w+)/$', 'date'),
    url(r'^(?P<city>\w+)/(?P<days>\w+)/$', 'theme'),
    url(r'^(?P<city>\w+)/(?P<days>\w+)/(?P<theme>\w+)/$', 'intensity'),
    url(r'^(?P<city>\w+)/(?P<days>\w+)/(?P<theme>\w+)/(?P<intensity>\w+)/$', 'luxury'),
)
