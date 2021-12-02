from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from dashboard.models import HealthFacility, Patient
from .serializers import (
    HealthFacilityDetailSerializer,
    HealthFacilityListSerializer,
    PatientCreateSerializer,
    PatientDetailSerializer,
    PatientListSerializer,
    HealthFacilityCreateSerializer,
)


class HealthFacilityCreateAPIView(CreateAPIView):
    """
    Create a New Facility
    """

    queryset = HealthFacility.objects.all()
    serializer_class = HealthFacilityCreateSerializer


class HealthFacilityListAPIView(ListAPIView):
    """
    List Facilities
    """

    queryset = HealthFacility.objects.all()
    serializer_class = HealthFacilityListSerializer


class HealthFacilityDetailAPIView(RetrieveAPIView):
    """
    Retrive Facility details
    """

    queryset = HealthFacility.objects.all()
    serializer_class = HealthFacilityDetailSerializer


class HealthFacilityUpdateAPIView(UpdateAPIView):
    """
    Update Facility details
    """

    queryset = HealthFacility.objects.all()
    serializer_class = HealthFacilityDetailSerializer


class HealthFacilityDeleteAPIView(DestroyAPIView):
    """
    Update Facility details
    """

    queryset = HealthFacility.objects.all()
    serializer_class = HealthFacilityDetailSerializer


class PatientListAPIView(ListAPIView):
    """
    List Patients
    """

    queryset = Patient.objects.all()
    serializer_class = PatientListSerializer


class PatientDetailAPIView(RetrieveAPIView):
    """
    Retrive Patient API View
    """

    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer


class PatientUpdateAPIView(UpdateAPIView):
    """
    Update Patient Details
    """

    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer


class PatientDeleteAPIView(DestroyAPIView):
    """
    Delete Patient Details
    """

    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer


class PatientCreateAPIView(CreateAPIView):
    """
    Register New Patient
    """

    queryset = Patient.objects.all()
    serializer_class = PatientCreateSerializer
