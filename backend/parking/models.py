from django.db import models
from django.utils import timezone

# Modèle de Place
class Place(models.Model):
    number = models.CharField(max_length=10, unique=True)  # Numéro de la place
    is_occupied = models.BooleanField(default=False)  # Statut de la place (libre/occupée)

    def __str__(self):
        return f"Place {self.number}"

# Modèle de Ticket
class Ticket(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)  # Référence à une place
    entry_time = models.DateTimeField(default=timezone.now)  # Heure d'entrée
    exit_time = models.DateTimeField(null=True, blank=True)  # Heure de sortie (peut être vide si toujours occupée)

    def __str__(self):
        return f"Ticket pour {self.place.number} - {self.entry_time} à {self.exit_time if self.exit_time else 'en cours'}"
