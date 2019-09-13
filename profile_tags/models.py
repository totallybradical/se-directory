from django.db import models

# Create your models here.
from django.conf import settings

# Model for a Profile Tag
class ProfileTag(models.Model):
    text = models.CharField(max_length=50)
    tag_color = models.CharField(max_length=6)

    class Meta:
        ordering = ['text']

    def add(self):
        self.save()

    def __str__(self):
        return self.text