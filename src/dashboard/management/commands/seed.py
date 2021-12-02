from dashboard.models import Location
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Data seeder"

    def handle(self, *args, **kwargs):
        self.stdout.write("seeding data...")
        create_locations()
        self.stdout.write("completed")


def create_locations():
    """
    Create Kenya Locations
    """
    locations = [
        "Mombasa",
        "Kwale",
        "Kilifi",
        "Tana River",
        "Lamu",
        "Taita-Taveta",
        "Garissa",
        "Wajir",
        "Mandera",
        "Marsabit",
        "Isiolo",
        "Meru",
        "Tharaka-Nithi",
        "Embu",
        "Kitui",
        "Machakos",
        "Makueni",
        "Nyandarua",
        "Nyeri",
        "Kirinyaga",
        "Muranga",
        "Kiambu",
        "Turkana",
        "West Pokot",
        "Samburu",
        "Trans-Nzoia",
        "Uasin Gishu",
        "Elgeyo-Marakwet",
        "Nandi",
        "Baringo",
        "Laikipia",
        "Nakuru",
        "Narok",
        "Kajiado",
        "Kericho",
        "Bomet",
        "Kakamega",
        "Vihiga",
        "Bungoma",
        "Busia",
        "Siaya",
        "Kisumu",
        "Homa Bay",
        "Migori",
        "Kisii",
        "Nyamira",
        "Nairobi",
    ]
    for x in locations:
        Location.objects.update_or_create(name=x)

    return "Done"
