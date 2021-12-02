from django.contrib import admin
from .models import HealthFacility, Patient, Location


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "gender",
        "age_group",
        "reg_month",
        "health_facility",
    ]


@admin.register(HealthFacility)
class HealthFacilityAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "location",
    ]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
