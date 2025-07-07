from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Movie, Director, Actor
from .forms import MovieForm, DirectorForm, ActorForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    template_name = 'login_form.html'
    
def index(request):
    movies = Movie.objects.all().order_by('year')
    actors = Actor.objects.all()
    directors = Director.objects.all()
    template = loader.get_template('index.html')
    context = {
        'title': 'Películas',
        'movies': movies,
        'actors': actors,
        'directors': directors
    }
    return HttpResponse(template.render(context, request))

def movies(request):
    movies = Movie.objects.all().order_by('year')
    template = loader.get_template('movies.html')
    context = {
        'title': 'Películas',
        'movies': movies
    }
    return HttpResponse(template.render(context, request))

def actors(request):
    actors = Actor.objects.all()
    template = loader.get_template('actors.html')
    context = {
        'title': 'Actores',
        'actors': actors
    }
    return HttpResponse(template.render(context, request))

def directors(request):
    directors = Director.objects.all()
    template = loader.get_template('directors.html')
    context = {
        'title': 'Directores',
        'directors': directors
    }
    return HttpResponse(template.render(context, request))


def movie(request, id):
    movie = Movie.objects.get(id=id)
    template = loader.get_template('movie.html')
    context = {
        'title': movie.title,
        'subtitle': movie.title,
        'banner': movie.banner,
        'movie': movie
    }
    return HttpResponse(template.render(context, request))

def actor(request, id):
    actor = Actor.objects.get(id=id)
    movies = actor.acted_movies.all()
    template = loader.get_template('actor.html')
    context = {
        'title': actor.name,
        'subtitle': actor.name,
        'actor': actor,
        'movies': movies
    }
    return HttpResponse(template.render(context, request))

def director(request, id):
    director = Director.objects.get(id=id)
    movies = director.directed_movies.all()
    template = loader.get_template('director.html')
    context = {
        'title': director.name,
        'subtitle': director.name,
        'director': director,
        'movies': movies
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_movie(request):
    context = {
        'title': 'Añadir película',
        'subtitle': 'Añadir película'
    }
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form, **context})

@login_required
def add_actor(request):
    context = {
        'title': 'Añadir actor',
        'subtitle': 'Añadir actor'
    }
    if request.method == 'POST':   
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = ActorForm()
    return render(request, 'actor_form.html', {'form': form, **context})

@login_required
def add_director(request):
    context = {
        'title': 'Añadir director',
        'subtitle': 'Añadir director'
    }
    if request.method == 'POST':
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = DirectorForm()
    return render(request, 'director_form.html', {'form': form, **context})

@login_required
def edit_movie(request, id: int):
    try:
        movie = Movie.objects.get(pk=id)
        context = {
            'title': f'Editar película: {movie.title}',
            'subtitle': f'Editar película: {movie.title}'
        }
        if request.method == 'POST':
            form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                movie = form.save(commit=False)
                if 'poster' in request.FILES:
                    movie.poster = request.FILES['poster']
                if 'banner' in request.FILES:
                    movie.banner = request.FILES['banner']
                movie.save()
                form.save_m2m()
                return redirect('movies:index')
            else:
                print("Errores del formulario:", form.errors)
        else:
            form = MovieForm(instance=movie)
        return render(request, 'movie_form.html', {'form': form, **context})
    except Movie.DoesNotExist:
        return redirect('movies:index')
    except Exception as e:
        print(f"Error al editar película: {e}")
        return redirect('movies:index')

@login_required
def edit_actor(request, id: int):
    try:
        actor = Actor.objects.get(pk=id)
        context = {
            'title': f'Editar actor: {actor.name}',
            'subtitle': f'Editar actor: {actor.name}'
        }
        if request.method == 'POST':
            form = ActorForm(request.POST, request.FILES, instance=actor)
            if form.is_valid():
                actor = form.save(commit=False)
                if 'photo' in request.FILES:
                    actor.photo = request.FILES['photo']
                actor.save()
                return redirect('movies:index')
            else:
                print("Errores del formulario:", form.errors)
        else:
            form = ActorForm(instance=actor)
        return render(request, 'actor_form.html', {'form': form, **context})
    except Actor.DoesNotExist:
        return redirect('movies:index')
    except Exception as e:
        print(f"Error al editar actor: {e}")
        return redirect('movies:index')

@login_required
def edit_director(request, id: int):
    try:
        director = Director.objects.get(pk=id)
        context = {
            'title': f'Editar director: {director.name}',
            'subtitle': f'Editar director: {director.name}'
        }
        if request.method == 'POST':
            form = DirectorForm(request.POST, request.FILES, instance=director)
            if form.is_valid():
                director = form.save(commit=False)
                if 'photo' in request.FILES:
                    director.photo = request.FILES['photo']
                director.save()
                return redirect('movies:index')
            else:
                print("Errores del formulario:", form.errors)
        else:
            form = DirectorForm(instance=director)
        return render(request, 'director_form.html', {'form': form, **context})
    except Director.DoesNotExist:
        return redirect('movies:index')
    except Exception as e:
        print(f"Error al editar director: {e}")
        return redirect('movies:index')

@login_required
def delete_movie(request, id: int):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect('movies:index')

@login_required
def delete_actor(request, id: int):
    actor = Actor.objects.get(pk=id)
    actor.delete()
    return redirect('movies:index')

@login_required
def delete_director(request, id: int):
    director = Director.objects.get(pk=id)
    director.delete()
    return redirect('movies:index')