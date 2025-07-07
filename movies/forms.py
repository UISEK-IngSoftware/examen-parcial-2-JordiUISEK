from django import forms
from datetime import datetime
from .models import Movie, Director, Actor

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'rating', 'duration', 'genre', 'banner', 'poster', 'description', 'directors', 'actors']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la película'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': str(datetime.now().year)}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 5, 'step': 0.1}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '0 minutos'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Género de la película'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción de la película'}),
            'directors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'actors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'poster': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'banner': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['poster'].required = False
        self.fields['banner'].required = False
        self.fields['rating'].required = False
        self.fields['duration'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('poster') and self.instance and self.instance.poster:
            cleaned_data['poster'] = self.instance.poster
        if not cleaned_data.get('banner') and self.instance and self.instance.banner:
            cleaned_data['banner'] = self.instance.banner
        
        if not cleaned_data.get('rating'):
            cleaned_data['rating'] = 0.0
        if not cleaned_data.get('duration'):
            cleaned_data['duration'] = 0
            
        return cleaned_data

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'nationality', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del director'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nacionalidad del director'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('photo') and self.instance and self.instance.photo:
            cleaned_data['photo'] = self.instance.photo
        return cleaned_data

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'nationality', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del actor'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nacionalidad del actor'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('photo') and self.instance and self.instance.photo:
            cleaned_data['photo'] = self.instance.photo
        return cleaned_data