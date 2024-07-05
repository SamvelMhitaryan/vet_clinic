from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Vet, Profession, Specialization, Achievements, Education
from .serializers import (VetSerializer, ProfessionSerializer, SpecializationSerializer,
                          AchievementsSerializer, EducationSerializer)


class VetViewSet(viewsets.ModelViewSet):
    queryset = Vet.objects.all()
    serializer_class = VetSerializer
    permission_classes = [IsAuthenticated]


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [IsAuthenticated]


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [IsAuthenticated]


class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer
    permission_classes = [IsAuthenticated]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]
