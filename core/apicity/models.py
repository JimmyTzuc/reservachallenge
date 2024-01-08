from django.db import models


class Key(models.Model):
    name_service = models.CharField(
        max_length=100,
    )
    private_key = models.CharField(max_length=100, null=True, blank=True)
    public_key = models.CharField(max_length=100)
