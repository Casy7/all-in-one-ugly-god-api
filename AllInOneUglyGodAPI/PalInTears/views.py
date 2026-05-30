from django.http import JsonResponse
from django.views import View
from .models import Location, Army, Character

class LocationDetailView(View):
    def get(self, request, pk=None):
        if pk:
            try:
                loc = Location.objects.get(pk=pk)
                return JsonResponse({
                    "id": loc.id, "name": loc.name, "description": loc.description,
                    "photo": loc.last_recorded_photo.url if loc.last_recorded_photo else None
                })
            except Location.DoesNotExist:
                return JsonResponse({"error": "location not found"}, status=404)
        
        # extract search query parameter
        q_query = request.GET.get('q', '')
        locations = Location.objects.filter(name__icontains=q_query)
        data = [{"id": l.id, "name": l.name, "description": l.description, "photo": l.last_recorded_photo.url if l.last_recorded_photo else None} for l in locations]
        return JsonResponse(data, safe=False)

class CharacterDetailView(View):
    def get(self, request, pk=None):
        if pk:
            try:
                char = Character.objects.get(pk=pk)
                return JsonResponse({
                    "id": char.id, "name": char.name, "race": char.race, "is_dangerous": char.is_dangerous,
                    "location": char.last_known_location.name if char.last_known_location else None,
                    "photo": char.last_recorded_photo.url if char.last_recorded_photo else None
                })
            except Character.DoesNotExist:
                return JsonResponse({"error": "character not found"}, status=404)
        
        # filter characters by name query
        q_query = request.GET.get('q', '')
        characters = Character.objects.filter(name__icontains=q_query)
        data = [{
            "id": c.id, "name": c.name, "race": c.race, "is_dangerous": c.is_dangerous,
            "location": c.last_known_location.name if c.last_known_location else None,
            "photo": c.last_recorded_photo.url if c.last_recorded_photo else None
        } for c in characters]
        return JsonResponse(data, safe=False)

class ArmyDetailView(View):
    def get(self, request, pk=None):
        if pk:
            try:
                army = Army.objects.get(pk=pk)
                return JsonResponse({
                    "id": army.id, "name": army.name, "faction": army.faction, "size": army.size,
                    "location": army.last_known_location.name if army.last_known_location else None,
                    "photo": army.last_recorded_photo.url if army.last_recorded_photo else None
                })
            except Army.DoesNotExist:
                return JsonResponse({"error": "army not found"}, status=404)
        
        # filter armies by name query
        q_query = request.GET.get('q', '')
        armies = Army.objects.filter(name__icontains=q_query)
        data = [{
            "id": a.id, "name": a.name, "faction": a.faction, "size": a.size,
            "location": a.last_known_location.name if a.last_known_location else None,
            "photo": a.last_recorded_photo.url if a.last_recorded_photo else None
        } for a in armies]
        return JsonResponse(data, safe=False)