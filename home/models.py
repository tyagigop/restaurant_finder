from django.db import models

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)  # Set primary_key=True for id field
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    items = models.JSONField()
    lat_long = models.CharField(max_length=50)
    full_details = models.JSONField()

    def __str__(self):
        return self.name
