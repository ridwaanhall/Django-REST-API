from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drinks_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({"drinks":serializer.data}, safe=False)