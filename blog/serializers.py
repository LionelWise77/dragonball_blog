from rest_framework import serializers
from .models import Secuela, Personaje, SecuelaImagen, Historia
from rest_framework.serializers import ImageField

class AbsoluteImageField(ImageField):
    def to_representation(self, value):
        request = self.context.get("request", None)
        url = super().to_representation(value)
        if request is not None:
            return request.build_absolute_uri(url)
        return url
    
class HistoriaSerializer(serializers.ModelSerializer):
    personajes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Historia
        fields = ['id', 'titulo', 'contenido', 'imagen_fondo', 'personajes','contenido_en', 'titulo_en',
                  'titulo_fr', 'contenido_fr']

class SecuelaImagenSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(use_url=True)
    
    
    class Meta:
        model = SecuelaImagen
        fields = ['id', 'imagen', 'descripcion']

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = [
            'id',
            'nombre',
            'descripcion',
            'imagen',
            'stamina',
            'velocidad',
            'caracter',
            'curiosidades',
        ]

class SecuelaSerializer(serializers.ModelSerializer):
    imagen_fondo = AbsoluteImageField()
    imagen_personaje = AbsoluteImageField()
    personajes = PersonajeSerializer(many=True, read_only=True)
    galeria = SecuelaImagenSerializer(many=True, read_only=True)

    class Meta:
        model = Secuela
        fields = [
            'id',
            'titulo',
            'contenido',
            'imagen_fondo',
            'imagen_personaje',
            'personajes',   # ✅ Personajes relacionados
            'galeria',      # ✅ Galería de imágenes tipo historieta
        ]
        
