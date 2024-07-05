from django.contrib import admin
from .models import Veterinerian, Profession, Specialization, Achievements, Education, Clinic, Service


@admin.register(Veterinerian)
class VeterinerianAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic')
    search_fields = ('name', 'surname', 'patronymic')
    filter_horizontal = ('professions', 'specializations',
                         'achievements', 'education')


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'work_time_start',
                    'work_time_end', 'phone', 'priority')
    search_fields = ('title', 'address', 'phone')
    list_filter = ('priority',)
    filter_horizontal = ('veterinerians',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'clinic')
    search_fields = ('title', 'clinic__title')
    list_filter = ('clinic',)
