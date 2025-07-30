from django.contrib import admin
from .models import Historia, Secuela, Personaje, SecuelaImagen

class SecuelaImagenInline(admin.TabularInline):
    model = SecuelaImagen
    extra = 1

@admin.register(Secuela)
class SecuelaAdmin(admin.ModelAdmin):
    inlines = [SecuelaImagenInline]
    list_display = ("titulo", "titulo_en", "titulo_fr")
    fieldsets = (
        ("Español", {
            "fields": ("titulo", "contenido", "mini_historia", "imagen_fondo", "imagen_personaje")
        }),
        ("Inglés", {
            "fields": ("titulo_en", "contenido_en", "mini_historia_en")
        }),
        ("Francés", {
            "fields": ("titulo_fr", "contenido_fr", "mini_historia_fr")
        }),
    )

@admin.register(Historia)
class HistoriaAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Español", {
            "fields": ("titulo", "contenido", "imagen_fondo")
        }),
        ("Inglés", {
            "fields": ("titulo_en", "contenido_en")
        }),
        ("Francés", {
            "fields": ("titulo_fr", "contenido_fr")
        }),
    )
@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nombre_en", "nombre_fr")
    search_fields = ("nombre", "nombre_en", "nombre_fr")
