from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Veterinerian, Profession, Specialization, Achievements, Education, Clinic, Service
from .serializers import (VeterinerianSerializer, ProfessionSerializer, SpecializationSerializer,
                          AchievementsSerializer, EducationSerializer, ClinicSerializer, ServiceSerializer)


class VeterinerianViewSet(viewsets.ModelViewSet):
    queryset = Veterinerian.objects.all()
    serializer_class = VeterinerianSerializer
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


class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = [IsAuthenticated]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
