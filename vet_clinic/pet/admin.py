from django.contrib import admin
from .models import Kind, Breed, Health, Procedures, Features, Pet, PetPhotos


@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind')
    search_fields = ('name', 'kind__name')
    list_filter = ('kind',)


@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    list_display = ('allergies', 'castration')
    list_filter = ('allergies', 'castration')


@admin.register(Procedures)
class ProceduresAdmin(admin.ModelAdmin):
    list_display = ('veterinarian_check', 'vaccination',
                    'deworming', 'tick_flea_treatmen')
    list_filter = ('veterinarian_check', 'vaccination',
                   'deworming', 'tick_flea_treatmen')


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'health')
    list_filter = ('name', 'health')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'breed', 'birthday', 'gender',
                    'weight', 'wool_type', 'chip_number', 'origin', 'master')
    search_fields = ('name', 'kind__name', 'breed__name',
                     'chip_number', 'master__username')
    list_filter = ('kind', 'breed', 'gender', 'wool_type', 'origin', 'master')


@admin.register(PetPhotos)
class PetPhotosAdmin(admin.ModelAdmin):
    list_display = ('pet', 'image', 'is_main')
    list_filter = ('pet', 'is_main')
