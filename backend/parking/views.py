from django.shortcuts import render, redirect
from .models import Place, Ticket
from django.http import HttpResponse
from django.utils import timezone
from django.http import JsonResponse


def list_places(request):
    places = Place.objects.all()
    places = Place.objects.all().values('id', 'is_occupied') 
    return JsonResponse(list(places), safe=False)


def get_ticket(request, place_id):
    place = Place.objects.get(id=place_id)
    if not place.is_occupied:


        ticket = Ticket(place=place)
        ticket.save()
        place.is_occupied = True
        place.save()
        return HttpResponse(f"Ticket créé pour la place {place.number}.")
    return HttpResponse("Cette place est déjà occupée.")


def release_place(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    place = ticket.place
    ticket.exit_time = timezone.now()
    ticket.save()
    place.is_occupied = False
    place.save()
    return HttpResponse(f"La place {place.number} a été libérée.")

def home():
    return render('parking/home.html')
