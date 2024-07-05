from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Kind, Breed, Health, Procedures, Features, Pet, PetPhotos
from .serializers import (KindSerializer, BreedSerializer, HealthSerializer,
                          ProceduresSerializer, FeaturesSerializer, PetSerializer, PetPhotosSerializer)


class KindViewSet(viewsets.ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer
    permission_classes = [IsAuthenticated]


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticated]


class HealthViewSet(viewsets.ModelViewSet):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    permission_classes = [IsAuthenticated]


class ProceduresViewSet(viewsets.ModelViewSet):
    queryset = Procedures.objects.all()
    serializer_class = ProceduresSerializer
    permission_classes = [IsAuthenticated]


class FeaturesViewSet(viewsets.ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer
    permission_classes = [IsAuthenticated]


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]


class PetPhotosViewSet(viewsets.ModelViewSet):
    queryset = PetPhotos.objects.all()
    serializer_class = PetPhotosSerializer
    permission_classes = [IsAuthenticated]
