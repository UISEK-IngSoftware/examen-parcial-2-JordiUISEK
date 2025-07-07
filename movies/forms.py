from django import forms
from datetime import datetime
from .models import Movie, Director, Actor

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'rating', 'duration', 'genre', 'banner', 'poster', 'description', 'directors', 'actors']
        widgets = {
            'title': forms.TextInput(attrs=({'class': 'form-control', 'placeholder': 'Título de la película'})),
            'year': forms.NumberInput(attrs=({'class': 'form-control', 'min': 0, 'placeholder': datetime.now().year})),
            'rating': forms.NumberInput(attrs=({'class': 'form-control', 'min': 0, 'max': 5, 'step': 0.1})),
            'duration': forms.NumberInput(attrs=({'class': 'form-control', 'min': 0, 'placeholder': '0 minutos'})),
            'genre': forms.TextInput(attrs=({'class': 'form-control', 'placeholder': 'Género de la película'})),
            'description': forms.Textarea(attrs=({'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción de la película'})),
            'directors': forms.SelectMultiple(attrs=({'class': 'form-control', 'placeholder': 'Directores de la película'})),
            'actors': forms.SelectMultiple(attrs=({'class': 'form-control', 'placeholder': 'Actores de la película'})),
            'poster': forms.FileInput(attrs=({'class': 'form-control', 'accept': 'image/*', 'placeholder': 'Poster de la película'})),
            'banner': forms.FileInput(attrs=({'class': 'form-control', 'accept': 'image/*', 'placeholder': 'Banner de la película'})),
        }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'nationality', 'photo']
        widgets = {
            'name': forms.TextInput(attrs=({'class': 'form-control mb-3', 'placeholder': 'Nombre del director'})),
            'nationality': forms.TextInput(attrs=({'class': 'form-control mb-3', 'placeholder': 'Nacionalidad del director'})),
            'photo': forms.FileInput(attrs=({'class': 'form-control', 'accept': 'image/*', 'placeholder': 'Foto del director'})),
        }

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'nationality', 'photo']
        widgets = {
            'name': forms.TextInput(attrs=({'class': 'form-control mb-3', 'placeholder': 'Nombre del actor'})),
            'nationality': forms.TextInput(attrs=({'class': 'form-control mb-3', 'placeholder': 'Nacionalidad del actor'})),
            'photo': forms.FileInput(attrs=({'class': 'form-control', 'accept': 'image/*', 'placeholder': 'Foto del actor'})),
        }