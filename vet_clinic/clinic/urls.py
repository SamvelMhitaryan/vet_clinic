from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (VeterinerianViewSet, ProfessionViewSet, SpecializationViewSet,
                    AchievementsViewSet, EducationViewSet, ClinicViewSet, ServiceViewSet)

router = DefaultRouter()
router.register(r'veterinerians', VeterinerianViewSet)
router.register(r'professions', ProfessionViewSet)
router.register(r'specializations', SpecializationViewSet)
router.register(r'achievements', AchievementsViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'clinics', ClinicViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
