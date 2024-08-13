from rest_framework import viewsets
from .models import Usuario, Beneficiario, Chaleco
from .serializers import UsuarioSerializer, BeneficiarioSerializer, ChalecoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class BeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer

class ChalecoViewSet(viewsets.ModelViewSet):
    queryset = Chaleco.objects.all()
    serializer_class = ChalecoSerializer
