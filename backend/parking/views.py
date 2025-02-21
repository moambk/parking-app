from .models import Place
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json



def list_places(request):
    places = Place.objects.all()
    places = Place.objects.all().values('id', 'is_occupied') 
    return JsonResponse(list(places), safe=False)


@api_view(['POST', 'PUT', 'PATCH'])
def update_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    if request.method == "PATCH":
        data = json.loads(request.body)
        place.is_occupied = data.get("is_occupied", place.is_occupied)
        place.save()
        return JsonResponse({"message": "Place mise à jour avec succès", "is_occupied": place.is_occupied})
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)




class TicketPurchaseView(APIView):
    def post(self, request, place_id):
        try:

            place = Place.objects.get(id=place_id)
            

            if place.is_occupied:
                return Response({"detail": "La place est déjà occupée."}, status=status.HTTP_400_BAD_REQUEST)
            
            place.is_occupied = True
            place.save()

            return Response({"detail": "Ticket acheté avec succès !"}, status=status.HTTP_200_OK)
        except Place.DoesNotExist:
            return Response({"detail": "Place non trouvée."}, status=status.HTTP_404_NOT_FOUND)
