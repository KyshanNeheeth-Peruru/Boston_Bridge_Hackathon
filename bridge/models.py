from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return self.name

