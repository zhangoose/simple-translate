from django.db import models

from django.utils.timezone import now


class Translation(models.Model):
    original_text = models.TextField()
    translated_text = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True, default=now)

