from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, BeneficiarioViewSet, ChalecoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'beneficiarios', BeneficiarioViewSet)
router.register(r'chalecos', ChalecoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
