import datetime

import requests

import decimal
import hashlib

from urllib import parse
from urllib.parse import urlparse

from telegramBot.models import BotSettings, Payment, TelegramUser
from telebot import TeleBot


# Создание подписи
def calculate_signature(*args) -> str:
    return hashlib.md5(':'.join(str(arg) for arg in args).encode()).hexdigest()


# Формирование URL переадресации пользователя на оплату.
def generate_payment_link(
    merchant_login: str,  # Логин магазина
    merchant_password: str,  # Пароль магазина
    cost: decimal,  # Цена
    number,  # Номер заказа
    description: str,  # Описание заказа
    ) -> str:

    # Генерация подписи (signature)
    signature = calculate_signature(
        merchant_login,
        cost,
        number,
        merchant_password
    )

    robokassa_payment_url = 'https://auth.robokassa.ru/Merchant/Index.aspx'

    data = {
        'MerchantLogin': merchant_login,
        'OutSum': cost,
        'InvId': number,
        'Description': description,
        'SignatureValue': signature,
        'Recurring': "true"
    }
    return f'{robokassa_payment_url}?{parse.urlencode(data)}'


def result_payment(request):
    param_request = request.POST.dict()
    cost = param_request['OutSum']
    number = param_request['InvId']
    signature = param_request['SignatureValue']

    bot_settings = BotSettings.objects.filter().first()

    new_signature = calculate_signature(cost, number, bot_settings.password_shop_2)

    if signature.lower() == new_signature.lower():
        payment = Payment.objects.filter(invoice_number=int(number)).first()
        if payment is None:
            return 'bad sign'

        payment.status = True
        payment.save()
        user = payment.user
        user.subscription = payment.subscription
        user.date_sub = datetime.datetime.now()
        if payment.maternity_payment:
            user.auto_payment = True
            user.previous_invoice_id = number
        user.save()

        
        bot = TeleBot(bot_settings.token)
        bot.send_message(user.user_id, "успех!")

        return 'OK{}'.format(number)
    else:
        return 'bad sign'



def recurring_payment(user_pk):
    url = 'https://auth.robokassa.ru/Merchant/Recurring'

    bot_settings: BotSettings = BotSettings.objects.filter().first()
    user = TelegramUser.objects.filter(pk=user_pk).first()



    invoice_number = bot_settings.invoice_number + 1

    signature = calculate_signature(
        bot_settings.id_shop,
        user.subscription.price,
        invoice_number,
        bot_settings.password_shop_1
    )

    payload = {'MerchantLogin': f'{bot_settings.id_shop}',
               'InvoiceID': f'{invoice_number}',
               'PreviousInvoiceID': f'{user.previous_invoice_id}',
               'Description': f'{user.subscription.description}',
               'SignatureValue': f'{signature}',
               'OutSum': f'{user.subscription.price}'}
    files = []
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    
    payment = Payment.objects.create(
        subscription=user.subscription,
        user=user,
        invoice_number=invoice_number,
        maternity_payment=False
    )

    bot_settings.invoice_number += 1
    bot_settings.save()

    bot = TeleBot(bot_settings.token)
    bot.send_message(user.user_id, "успех!")

    return response