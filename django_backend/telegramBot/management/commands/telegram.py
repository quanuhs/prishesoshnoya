from django.core.management.base import BaseCommand

from telegramBot.models import BotSettings
from telegramBot.logic.handle_request import handle_longpoll

class Command(BaseCommand):
    # если планируете использовать longpoll
    def handle(self, *args, **options):
         settings = BotSettings.objects.first()
         print("Longpoll bot is up")
         handle_longpoll(settings)
         print("Longpoll bot is down")
