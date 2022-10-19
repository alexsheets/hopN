"""
a brewery should have its own name, description, address,
perhaps add one-to-one and one-to-many type fields later
in prod
"""

from django.db import models

# Create your models here.
class Brewery(models.Model):
    # breweries must have name
    name = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(max_length=80, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    img = models.ImageField()
    phn_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=150, blank=True)


