from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import date_based
from artsy.models import Artwork
admin.autodiscover()

artwork_info = {
	"queryset" : Artwork.objects.all(),
	"date_field" : "date_Uploaded"
}

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'artsy.views.index', name='index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^artists/$', 'artsy.views.artist_list'),
	url(r'^artist/(?P<username>[-\.\w]+)/$', 'artsy.views.artist_detail'),
	url(r'^artwork/(?P<username>/?P<slug>[-\w]+)/$', 'artsy.views.artwork_detail'),
	#url(r'^artwork/$', date_based.archive_index, artwork_info),
	url(r'^artwork/$', 'django.views.generic.date_based.archive_index', 
  {
      'queryset': Artwork.objects.all(), 
      'date_field': 'date_Uploaded', 
      'template_name': 'artsy/artwork_list.html'}
      ),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
