from rest_framework import viewsets
from .models import Historia, Secuela, Personaje
from .serializers import HistoriaSerializer, SecuelaSerializer, PersonajeSerializer

class HistoriaViewSet(viewsets.ModelViewSet):
    queryset = Historia.objects.all()
    serializer_class = HistoriaSerializer

class SecuelaViewSet(viewsets.ModelViewSet):
    queryset = Secuela.objects.all()
    serializer_class = SecuelaSerializer
    
    def get_serializer_context(self):
        return {"request": self.request}
    
class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer    
