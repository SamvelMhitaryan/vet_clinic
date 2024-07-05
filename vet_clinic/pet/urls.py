from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (KindViewSet, BreedViewSet, HealthViewSet, ProceduresViewSet,
                    FeaturesViewSet, PetViewSet, PetPhotosViewSet)

router = DefaultRouter()
router.register(r'kinds', KindViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'health', HealthViewSet)
router.register(r'procedures', ProceduresViewSet)
router.register(r'features', FeaturesViewSet)
router.register(r'pets', PetViewSet)
router.register(r'petphotos', PetPhotosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
