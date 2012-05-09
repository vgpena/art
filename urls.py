from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'art.views.artist_list'),
	url(r'^artist/(?P<username>[-\.\w]+)/$', 'art.views.artist_detail'),
	url(r'^artwork/(?P<slug>[-\w]+)/$', 'art.views.artwork_detail'),
)
