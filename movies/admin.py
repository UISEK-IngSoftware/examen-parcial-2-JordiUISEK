from django.contrib import admin
from .models import Movie, Director, Actor  

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'rating', 'duration', 'genre', 'banner', 'poster', 'description', 'get_directors', 'get_actors')
    def get_actors(self, obj):
        return ", ".join([actor.name for actor in obj.actors.all()])
    get_actors.short_description = 'Actores'
    def get_directors(self, obj):
        return ", ".join([director.name for director in obj.directors.all()])
    get_directors.short_description = 'Directores'
    pass

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'photo')
    pass

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'photo')
    pass
