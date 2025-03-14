import os
import json
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import src.core.models as models


class Command(BaseCommand):
    help = "Install first model data and createsuperuser"

    def handle(self, *args, **options):
        os.system("python3 manage.py makemigrations")
        os.system("python3 manage.py migrate")
        with open('src/resources/city.json', "r") as data:
            city = json.load(data)
            for i in city:
                if not models.City.objects.filter(external_id=i.get("id")).exists():
                    models.City.objects.create(
                        external_id=i.get("id"),
                        name=i.get("name"),
                        latitude=i.get("coord").get("lat"),
                        longitude=i.get("coord").get("lon")
                    )
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"City ID: {i.get('id')}, NAME: {i.get('name')} added"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f"City ID: {i.get('id')}, NAME: {i.get('name')} already exists"
                        )
                    )
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                password="123"
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "Superuser created\n\nusername: admin\npassword:123"
                )
            )
        if not settings.DOCKER:
            os.system("python3 manage.py runserver")
