from django.http import JsonResponse
from .models import KeystrokeLog
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Disable CSRF for simplicity in this case
def log_keystroke(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        key = data.get('key')
        if key:
            KeystrokeLog.objects.create(key=key)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'No key provided'})
    return JsonResponse({'status': 'error', 'message': 'Invalid method'})
