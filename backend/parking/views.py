from django.shortcuts import render, redirect
from .models import Place, Ticket
from django.http import HttpResponse
from django.utils import timezone

# Afficher toutes les places (libres et occupées)
def list_places(request):
    places = Place.objects.all()
    return render(request, 'parking/places_list.html', {'places': places})

# Obtenir un ticket pour une place
def get_ticket(request, place_id):
    place = Place.objects.get(id=place_id)
    if not place.is_occupied:
        # Créer un ticket et marquer la place comme occupée
        ticket = Ticket(place=place)
        ticket.save()
        place.is_occupied = True
        place.save()
        return HttpResponse(f"Ticket créé pour la place {place.number}.")
    return HttpResponse("Cette place est déjà occupée.")

# Libérer une place
def release_place(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    place = ticket.place
    ticket.exit_time = timezone.now()
    ticket.save()
    place.is_occupied = False
    place.save()
    return HttpResponse(f"La place {place.number} a été libérée.")


