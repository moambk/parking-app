from django.db import models
from django.utils import timezone


class Place(models.Model):
    number = models.CharField(max_length=10, unique=True)  
    is_occupied = models.BooleanField(default=False)  

    def __str__(self):
        return f"Place {self.number}"


class Ticket(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)  
    entry_time = models.DateTimeField(default=timezone.now)  
    exit_time = models.DateTimeField(null=True, blank=True)  

    def __str__(self):
        return f"Ticket pour {self.place.number} - {self.entry_time} à {self.exit_time if self.exit_time else 'en cours'}"
