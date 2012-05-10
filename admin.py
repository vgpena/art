from artsy.models import Artist, Artwork
from django.contrib import admin

class ArtworkAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Artist)
#admin.site.register(Artwork)
admin.site.register(Artwork, ArtworkAdmin)
