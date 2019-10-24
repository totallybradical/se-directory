from django.db import models

# Create your models here.
from profile_tags.models import ProfileTag
from django.conf import settings


class Profile(models.Model):
    name = models.CharField(max_length=200)
    cec = models.CharField(max_length=25)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    GEOS = [
        ("APJC", "APJC"),
        ("EMEAR", "EMEAR"),
        ("GLOBE", "Global"),
        ("LATAM", "LATAM"),
        ("TEMP", "TEMP"),
        ("USCAN", "Americas")
    ]
    geo = models.CharField(
        max_length=5,
        choices=GEOS
    )
    TEAMS = [
        ("TEMP", "TEMP"),
        ("COMM", "Commercial"),
        ("USPS", "Public Sector")
    ]
    team = models.CharField(
        max_length=4,
        choices=TEAMS
    )
    REGIONS = [
        ("A", "All"),
        ("C", "Central"),
        ("E", "East"),
        ("O", "Other"),
        ("S", "South"),
        ("W", "West")
    ]
    region = models.CharField(
        max_length=1,
        choices=REGIONS
    )
    STRENGTHS = [
        ("ADV", "Advisor"),
        ("CON", "Connector"),
        ("CRE", "Creator"),
        ("EQU", "Equalizer"),
        ("INF", "Influencer"),
        ("PIO", "Pioneer"),
        ("PRO", "Provider"),
        ("STI", "Stimulator"),
        ("TEA", "Teacher"),
        ("UNK", "Unknown")
    ]
    primary_strength = models.CharField(
        max_length=3,
        choices=STRENGTHS
    )
    secondary_strength = models.CharField(
        max_length=3,
        choices=STRENGTHS
    )
    tags = models.ManyToManyField(ProfileTag)

    class Meta:
        ordering = ['name']
    
    def add(self):
        self.save()

    def __str__(self):
        return self.name