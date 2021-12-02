from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from dashboard.models import Patient, HealthFacility, Location


class HealthFacilityListSerializer(ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = [
            "name",
            "location",
        ]


class HealthFacilityDetailSerializer(ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = "__all__"


class HealthFacilityCreateSerializer(ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = ["name", "location"]


class PatientListSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "name",
            "gender",
            "age_group",
            "location",
            "health_facility",
            "reg_month",
        ]


class PatientDetailSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientCreateSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "name",
            "gender",
            "age_group",
            "location",
            "health_facility",
            "reg_month",
        ]
