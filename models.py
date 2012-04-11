from django.db import models
from django.contrib.auth.models import User

class Artist(User):
	YEAR_CHOICES = (
		('First-year', 'First-year'),
		('Second-year', 'Second-year'),
		('Third-year', 'Third-year'),
		('Fourth-year', 'Fourth-year'),
		('Fifth-year', 'Fifth-year'),
		('Graduate', 'Graduate'),
	)
	
	hometown = models.CharField(max_length = 30, null = True)
	gender = models.CharField(max_length = 20, null = True)
	age = models.IntegerField(max_length = 3)
	Year = models.CharField(max_length = 12, choices = YEAR_CHOICES)
	Majors = models.CharField(max_length = 255, null = True)
	Minors = models.CharField(max_length = 255, null= True)
	favoriteArtists = models.CharField(max_length = 255, null = True)
	interests = models.CharField(max_length = 255, null = True)
	height = models.IntegerField() 
  	width = models.IntegerField()
	#avatar = models.ImageField(upload_to = "/avatars/", height_field='height', width_field='width', null = True)

	def __unicode__(self):
		return self.username
		
class Artwork(models.Model):
	title = models.CharField(max_length = 30, null = False)
	slug = models.SlugField(max_length = 30)
	height = models.IntegerField() 
  	width = models.IntegerField()
	#artwork = models.ImageField(upload_to="/art/", height_field='height', width_field='width')
	open = models.BooleanField()
	originalArtist = models.ForeignKey(User, related_name = 'original work')
	otherArtists = models.ManyToManyField(User, null = True)
	dateUploaded = models.DateTimeField(auto_now_add = True)
	dateModified = models.DateTimeField(auto_now = True)
	description = models.TextField()
	
	
	def __unicode__(self):
		return self.title