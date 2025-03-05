from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DataEntry

def home(request):
    # This will render the template located at my_app/templates/my_app/home_page.html
    return render(request, 'my_app/home_page.html')

@csrf_exempt  # For testing only; adjust CSRF for production
def receive_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            data_value = data.get('data')
            DataEntry.objects.create(data_column=data_value)
            return JsonResponse({'message': 'Data inserted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
