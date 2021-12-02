from django.shortcuts import render
from django.views.generic import View
from .models import Location, Patient, HealthFacility


class HomeView(View):
    """
    Home dashboard view
    """

    def get(self, request):
        facilities = HealthFacility.objects.all()
        for facility in facilities:
            data = {
                "total": facility.total_patients,
            }
        return render(request, "dashboard/index.html", context={})
