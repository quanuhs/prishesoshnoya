import json

from django.http import HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from .models import BotSettings
from .logic.handle_request import handle



@csrf_exempt
def handle_telegram(request, secret_key):
    
    settings = BotSettings.objects.filter(webhook_secret=secret_key).first()
    if settings is None:
        return HttpResponse("API key is invalid!", content_type="text/plain", status=403)

    handle(request, settings)

    return HttpResponse('OK', content_type="text/plain", status=200)