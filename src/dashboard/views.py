from django.shortcuts import render
from django.views.generic import View
from .models import Location, Patient, HealthFacility


def index(request):
    facilities = HealthFacility.objects.all()
    patients = Patient.objects.all()
    locations = Location.objects.all()

    total_facilities = facilities.count()
    total_patients = patients.count()
    total_locations = 47

    labels = []
    data = []

    genders = ["male", "female"]

    for gender in genders:
        labels.append(gender)
        data.append(Patient.objects.filter(gender=gender).count())

    context = {
        "facilities": facilities,
        "total_facilities": total_facilities,
        "patients": total_patients,
        "locations": total_locations,
        "labels": labels,
        "data": data,
    }

    return render(request, "dashboard/index.html", context=context)


def facilities_detail(request):
    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]
    facilities = HealthFacility.objects.all()
    res_data = []
    for facility in facilities:
        res = []
        for month in months:
            data = {
                "month": month,
                "total": facility.total_reg_per_month(month),
            }
        res.append(data)
        fc_data = {
            "facility": facility.name,
            "data": res,
        }
    res_data.append(fc_data)

    context = {"res_data": res_data}
    return render(request, "dashboard/index.html", context=context)
