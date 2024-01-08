from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from apicity.models import Key


class Command(BaseCommand):
    help = "Populate Database"

    def seeder_database(self):
        User = get_user_model()

        User.objects.create_user(
            "admin",
            "admin@admin.com",
            "admin",
            **{"is_active": True, "is_staff": True, "is_superuser": True}
        )

        Key.objects.create(
            name_service="weather",
            public_key="45b95443f43ab6762c4b4b153d9e261f",
            private_key=""
        )

    def handle(self, *args, **options):
        self.seeder_database()
