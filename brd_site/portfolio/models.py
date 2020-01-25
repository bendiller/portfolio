from django.db import models


class Project(models.Model):
    name = models.CharField(blank=False, max_length=64, primary_key=True, unique=True)
    start_date = models.DateField(blank=False)
    stop_date = models.DateField(blank=True)
    short_blurb = models.TextField(blank=False)
    long_blurb = models.TextField(blank=False)
    code_link = models.URLField(blank=True)
