from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='media/photos')

class Artist(User):
	YEAR_CHOICES = (
		('First-year', 'First-year'),
		('Second-year', 'Second-year'),
		('Third-year', 'Third-year'),
		('Fourth-year', 'Fourth-year'),
		('Fifth-year', 'Fifth-year'),
		('Graduate', 'Graduate'),
	)
	
	hometown = models.CharField(max_length = 30, null = True, blank=True)
	gender = models.CharField(max_length = 20, null = True, blank=True)
	age = models.IntegerField(max_length = 3, blank=True)
	year = models.CharField(max_length = 12, choices = YEAR_CHOICES, blank=True)
	majors = models.CharField(max_length = 255, null = True, blank=True)
	minors = models.CharField(max_length = 255, null= True, blank=True)
	favorite_artists = models.CharField(max_length = 255, null = True, blank=True)
	interests = models.CharField(max_length = 255, null = True, blank=True)
	#height = models.IntegerField(null=True, blank = True) 
  	#width = models.IntegerField(null=True, blank = True)
  	
	avatar = models.ImageField(storage=fs, upload_to="avatars/", null = True, blank = True)

	def __unicode__(self):
		return self.username
		
class Artwork(models.Model):
	title = models.CharField(max_length = 30, null = False, blank=False)
	slug = models.SlugField(max_length = 30)
	#height = models.IntegerField() 
  	#width = models.IntegerField()
	artwork = models.ImageField(upload_to="art/")
	is_open = models.BooleanField()
	original_artist = models.ForeignKey(User, related_name = 'original work')
	other_artists = models.ManyToManyField(User, null = True, blank=True)
	date_Uploaded = models.DateTimeField(auto_now_add = True)
	date_Modified = models.DateTimeField(auto_now = True)
	description = models.TextField(blank=True)
	
	
	def __unicode__(self):
		return self.title