from rest_framework import serializers
from .models import Kind, Breed, Health, Procedures, Features, Pet, PetPhotos


class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'


class ProceduresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedures
        fields = '__all__'


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class PetPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetPhotos
        fields = '__all__'
