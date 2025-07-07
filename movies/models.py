from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, null=False)
    year = models.IntegerField(null=False)
    rating = models.FloatField(default=0.0)
    duration = models.IntegerField(default=0, null=False)
    genre = models.CharField(max_length=200, null=False)
    poster = models.ImageField(upload_to='movie_images/', null=True)
    banner = models.ImageField(upload_to='movie_images/', null=True)
    description = models.TextField(null=False)
    directors = models.ManyToManyField('Director', related_name='directed_movies')
    actors = models.ManyToManyField('Actor', related_name='acted_movies')

class Director(models.Model):
    name = models.CharField(max_length=200, null=False)
    nationality = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='director_images/', null=True)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=200, null=False)
    nationality = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='actor_images/', null=True)

    def __str__(self):
        return self.name