import json

from django.http import HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from telegramBot.models import BotSettings, RobokassaLogs
from telegramBot.robokassa_api import result_payment
from .logic.handle_request import handle_webhook



@csrf_exempt
def handle_telegram(request, secret_key):
    
    settings = BotSettings.objects.filter(webhook_secret=secret_key).first()
    if settings is None:
        return HttpResponse("API key is invalid!", content_type="text/plain", status=403)

    handle_webhook(request, settings)

    return HttpResponse('OK', content_type="text/plain", status=200)


@csrf_exempt
def robokassa_result(request):
    RobokassaLogs.objects.create(text=str(request.POST.dict()))
    return HttpResponse(result_payment(request))