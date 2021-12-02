from django.urls import path

from .views import (
    HealthFacilityCreateAPIView,
    HealthFacilityDeleteAPIView,
    HealthFacilityDetailAPIView,
    HealthFacilityListAPIView,
    HealthFacilityUpdateAPIView,
    PatientDeleteAPIView,
    PatientDetailAPIView,
    PatientListAPIView,
    PatientUpdateAPIView,
    PatientCreateAPIView,
)

app_name = "dashboard_api"

urlpatterns = [
    path("facilities/", HealthFacilityListAPIView.as_view(), name="facilities"),
    path(
        "facility/<int:pk>/",
        HealthFacilityDetailAPIView.as_view(),
        name="facility_detail",
    ),
    path(
        "facility/<int:pk>/update/",
        HealthFacilityUpdateAPIView.as_view(),
        name="facility_update",
    ),
    path(
        "facility/<int:pk>/delete/",
        HealthFacilityDeleteAPIView.as_view(),
        name="facility_delete",
    ),
    path(
        "facility/create",
        HealthFacilityCreateAPIView.as_view(),
        name="facility_create",
    ),
    path("patients/", PatientListAPIView.as_view(), name="patients"),
    path(
        "patient/<int:pk>/",
        PatientDetailAPIView.as_view(),
        name="patient_detail",
    ),
    path(
        "patient/<int:pk>/update/",
        PatientUpdateAPIView.as_view(),
        name="patient_update",
    ),
    path(
        "patient/<int:pk>/delete/",
        PatientDeleteAPIView.as_view(),
        name="patient_delete",
    ),
    path("patient/register/", PatientCreateAPIView.as_view(), name="patient_create"),
]
