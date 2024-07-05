from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (VetViewSet, ProfessionViewSet, SpecializationViewSet,
                    AchievementsViewSet, EducationViewSet)

router = DefaultRouter()
router.register(r'vets', VetViewSet)
router.register(r'professions', ProfessionViewSet)
router.register(r'specializations', SpecializationViewSet)
router.register(r'achievements', AchievementsViewSet)
router.register(r'education', EducationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
