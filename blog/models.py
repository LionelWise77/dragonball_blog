from django.db import models
from django.core.exceptions import ValidationError

class Historia(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    imagen_fondo = models.ImageField(upload_to="historias/")
    titulo_en = models.CharField(max_length=255, blank=True, null=True)
    contenido_en = models.TextField(blank=True, null=True)
    titulo_fr = models.CharField(max_length=255, blank=True, null=True)
    contenido_fr = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Secuela(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_en = models.CharField(max_length=200, blank=True, null=True)
    titulo_fr = models.CharField(max_length=200, blank=True, null=True)
    
    contenido = models.TextField()
    contenido_en = models.TextField(blank=True, null=True)
    contenido_fr = models.TextField(blank=True, null=True)
    
    mini_historia = models.TextField(blank=True, null=True)
    mini_historia_en = models.TextField(blank=True, null=True)
    mini_historia_fr = models.TextField(blank=True, null=True)
    
    imagen_fondo = models.ImageField(upload_to="secuelas/")
    imagen_personaje = models.ImageField(upload_to="personajes/")
    
    def __str__(self):
        return self.titulo

class Personaje(models.Model):
    nombre = models.CharField(max_length=255)
    nombre_en = models.CharField(max_length=255, blank=True, null=True)
    nombre_fr = models.CharField(max_length=255, blank=True, null=True)
    
    descripcion = models.TextField()
    descripcion_en = models.TextField(blank=True, null=True)
    descripcion_fr = models.TextField(blank=True, null=True)
    
    imagen = models.URLField(blank=True, null=True)

    historia = models.ForeignKey(
        "Historia", related_name="personajes", on_delete=models.CASCADE, blank=True, null=True
    )
    secuela = models.ForeignKey(
        "Secuela", related_name="personajes", on_delete=models.CASCADE, blank=True, null=True
    )

    # NUEVOS CAMPOS
    stamina = models.IntegerField(default=0)
    velocidad = models.IntegerField(default=0)
    caracter = models.CharField(max_length=100, blank=True)
    curiosidades = models.TextField(blank=True)

    def clean(self):
        # Asegura que el personaje esté asociado a historia o secuela, pero no a ambas
        if not self.historia and not self.secuela:
            raise ValidationError("Un personaje debe estar asociado a una historia o una secuela.")
        if self.historia and self.secuela:
            raise ValidationError("Un personaje no puede estar asociado a historia y secuela al mismo tiempo.")

    def __str__(self):
        return self.nombre
    
    
class SecuelaImagen(models.Model):
    secuela = models.ForeignKey(Secuela, related_name="galeria", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="secuelas/galeria/")
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Imagen de {self.secuela.titulo}- {self.descripcion or 'sin descripción'}"
    