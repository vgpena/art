from django.views.generic import DetailView, ListView
from art.models import Artist, Artwork


class ArtistDetailView(DetailView):
	model = Artist
	
	def get_object(self):
		return self.model.objects.get(username=self.kwargs['username'])


class ArtistListView(ListView):
	model = Artist


class ArtworkDetailView(DetailView):
	model = Artwork


artist_detail = ArtistDetailView.as_view()
artist_list = ArtistListView.as_view()
artwork_detail = ArtworkDetailView.as_view()