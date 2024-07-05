from django.contrib import admin
from .models import Vet, Profession, Specialization, Achievements, Education


@admin.register(Vet)
class VetAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic')
    search_fields = ('name', 'surname', 'patronymic')


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'vet')
    search_fields = ('name', 'vet__name')
    list_filter = ('vet',)


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('name', 'vet')
    search_fields = ('name', 'vet__name')
    list_filter = ('vet',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'vet')
    search_fields = ('name', 'vet__name')
    list_filter = ('vet',)
