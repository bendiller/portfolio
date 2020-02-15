from django.db import models


class Project(models.Model):

    class ProjType(models.TextChoices):
        PERSONAL = "Personal"
        OPEN_SOURCE = "OpenSource"

    name = models.CharField(blank=False, max_length=64, primary_key=True, unique=True)
    start_date = models.DateField(blank=False)
    stop_date = models.DateField(blank=True, null=True)
    short_blurb = models.TextField(blank=False)
    long_blurb = models.TextField(blank=False)
    code_link = models.URLField(blank=True, null=True)
    type = models.CharField(blank=False, choices=ProjType.choices, default=ProjType.PERSONAL, max_length=16)

    @property
    def start_date_as_str(self):
        return self.format_date(self.start_date)

    @property
    def stop_date_as_str(self):
        return self.format_date(self.stop_date) if self.stop_date else "Present"

    @staticmethod
    def format_date(date_field):
        """Format DateField representations to remove day of month."""
        return date_field.strftime('%b %Y')


class TechTag(models.Model):
    name = models.CharField(blank=False, max_length=64, primary_key=True, unique=True)
    projects = models.ManyToManyField(Project)

    class Meta:
        ordering = ['name']


class Content(models.Model):
    name = models.CharField(blank=False, max_length=32, unique=True)
    text = models.TextField(blank=False)
