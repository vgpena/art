from django.views.generic import DetailView, ListView, TemplateView, date_based
from django.shortcuts import render_to_response
from artsy.models import Artist, Artwork


class ArtistDetailView(DetailView):
	model = Artist
	
	def get_object(self):
		return self.model.objects.get(username=self.kwargs['username'])


class ArtistListView(ListView):
	model = Artist

class ArtworkDetailView(DetailView):
	model = Artwork
	
class ArtworkListView(ListView):
	model = Artwork
	
class IndexView(TemplateView):
	template_name = 'artsy/index.html'

artist_detail = ArtistDetailView.as_view()
artist_list = ArtistListView.as_view()
artwork_detail = ArtworkDetailView.as_view()
artwork_list = ArtworkListView.as_view()
index = IndexView.as_view()