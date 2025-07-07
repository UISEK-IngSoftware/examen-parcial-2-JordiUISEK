from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("movie/", views.movies, name="movies"),
    path("movie/<int:id>/", views.movie, name="movie"),
    path("movie/add/", views.add_movie, name="add_movie"),
    path("movie/edit/<int:id>/", views.edit_movie, name="edit_movie"),
    path("movie/delete/<int:id>/", views.delete_movie, name="delete_movie"),
    path("director/", views.directors, name="directors"),
    path("director/<int:id>/", views.director, name="director"),
    path("director/add/", views.add_director, name="add_director"),
    path("director/edit/<int:id>/", views.edit_director, name="edit_director"),
    path("director/delete/<int:id>/", views.delete_director, name="delete_director"),
    path("actor/", views.actors, name="actors"),
    path("actor/<int:id>/", views.actor, name="actor"),
    path("actor/add/", views.add_actor, name="add_actor"),
    path("actor/edit/<int:id>/", views.edit_actor, name="edit_actor"),
    path("actor/delete/<int:id>/", views.delete_actor, name="delete_actor"),
]