from django.db import models

# Create your models here.
from django.conf import settings


class Profile(models.Model):
    name = models.CharField(max_length=200)
    cec = models.CharField(max_length=25)
    TEAMS = [
        ("COMM", "Commercial"),
        ("USPS", "Public Sector")
    ]
    team = models.CharField(
        max_length=4,
        choices=TEAMS
    )
    REGIONS = [
        ("C", "Central"),
        ("S", "South"),
        ("E", "East"),
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
        ("TEA", "Teacher")
    ]
    primary_strength = models.CharField(
        max_length=3,
        choices=STRENGTHS
    )
    secondary_strength = models.CharField(
        max_length=3,
        choices=STRENGTHS
    )

    class Meta:
        ordering = ['name']
    
    def add(self):
        self.save()

    def __str__(self):
        return self.name