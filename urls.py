from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'artsy.views.artist_list'),
	url(r'^artist/(?P<username>[-\.\w]+)/$', 'artsy.views.artist_detail'),
	url(r'^artwork/(?P<slug>[-\w]+)/$', 'artsy.views.artwork_detail'),
)
