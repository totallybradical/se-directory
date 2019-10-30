from django.db import models

# Create your models here.
from profiles.models import Profile
from django.conf import settings

# Model for a factoid (not an instance of factoid)
class Factoid(models.Model):
    # Map to a specific profile
    profile =  models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_fun = models.BooleanField()

    def add(self):
        self.save()

    def __str__(self):
        return self.text