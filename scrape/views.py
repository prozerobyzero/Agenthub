from django.http import JsonResponse
from .models import Scrape

def scraped(request):
    scrapes = Scrape.objects.all().values('weblink', 'data', 'is_valid')
    return JsonResponse(list(scrapes), safe=False)


# Test endpoint to add hardcoded data
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_scrape(request):
    try:
        scrape = Scrape.objects.create(
            weblink='https://example.com',
            data='Sample scraped data',
            is_valid=True
        )
        return JsonResponse({'id': scrape.id, 'weblink': scrape.weblink, 'data': scrape.data, 'is_valid': scrape.is_valid}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
