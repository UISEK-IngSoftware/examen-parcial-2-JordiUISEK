from rest_framework import serializers
from movies.models import Movie, Actor, Director
import base64
from django.core.files.base import ContentFile

class MovieSerializer(serializers.ModelSerializer):
    poster = serializers.CharField(required=False, allow_blank=True)
    banner = serializers.CharField(required=False, allow_blank=True)
        
    class Meta:
        model = Movie
        fields = '__all__'
        
    def validate_poster(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile (
                    base64.b64decode(imgstr),
                    name=f'poster_temp.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Imagen no válida")
        return None
    
    def validate_banner(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile (
                    base64.b64decode(imgstr),
                    name=f'banner_temp.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Imagen no válida")
        return None
    
class ActorSerializer(serializers.ModelSerializer):
    photo = serializers.CharField(required=False, allow_blank=True)
        
    class Meta:
        model = Actor
        fields = '__all__'
        
    def validate_photo(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile (
                    base64.b64decode(imgstr),
                    name=f'actor_temp.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Imagen no válida")
        return None
    
class DirectorSerializer(serializers.ModelSerializer):
    photo = serializers.CharField(required=False, allow_blank=True)
        
    class Meta:
        model = Director
        fields = '__all__'
        
    def validate_photo(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile (
                    base64.b64decode(imgstr),
                    name=f'director_temp.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Imagen no válida")
        return None