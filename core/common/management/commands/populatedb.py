from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


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

    def handle(self, *args, **options):
        self.seeder_database()
