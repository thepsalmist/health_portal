from django.db import models


class Location(models.Model):
    """
    Locations in Kenya
    """

    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class HealthFacility(models.Model):
    """
    Various health facilities
    """

    name = models.CharField(max_length=256)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    @property
    def total_patients(self):
        return Patient.objects.filter(health_facility=self).count()

    @property
    def total_registrations_by_gender(self, gender):
        return Patient.objects.filter(health_facility=self, gender=gender).count()


class Patient(models.Model):
    """
    Model Patient data
    """

    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )
    AGE_GROUP_CHOICES = (
        ("1", "0-10"),
        ("2", "10-20"),
        ("3", "20-30"),
        ("4", "30-40"),
        ("5", "40-50"),
        ("6", "50-60"),
        ("7", "60-70"),
    )
    MONTH_CHOICES = (
        ("january", "January"),
        ("february", "February"),
        ("march", "March"),
        ("april", "April"),
        ("may", "May"),
        ("june", "June"),
        ("july", "July"),
        ("august", "August"),
        ("september", "Septemder"),
        ("october", "October"),
        ("november", "November"),
        ("december", "December"),
    )
    name = models.CharField(max_length=256)
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
    )
    age_group = models.CharField(
        max_length=10,
        choices=AGE_GROUP_CHOICES,
        default="1",
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    health_facility = models.ForeignKey(HealthFacility, on_delete=models.CASCADE)
    reg_month = models.CharField(
        max_length=200, choices=MONTH_CHOICES, default="january"
    )
