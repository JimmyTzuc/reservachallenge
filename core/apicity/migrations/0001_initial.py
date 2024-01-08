# Generated by Django 4.2.9 on 2024-01-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Key",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_service", models.CharField(max_length=100)),
                (
                    "private_key",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("public_key", models.CharField(max_length=100)),
            ],
        ),
    ]