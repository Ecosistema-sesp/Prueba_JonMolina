from rest_framework import serializers
from .models import Usuario, Beneficiario, Chaleco

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = '__all__'

class ChalecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chaleco
        fields = '__all__'
