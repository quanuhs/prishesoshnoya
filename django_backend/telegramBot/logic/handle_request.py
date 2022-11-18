import telebot
from telebot import types
from telegramBot.models import BotDictionary, TelegramUser

from telegramBot.logic.markups import Markups



class TelegramBot(telebot.TeleBot):
    settings = None
    
    def set_token(self, new_token):
        self.token = new_token
    
    def set_settings(self, settings):
        self.settings = settings


bot: TelegramBot = TelegramBot(None)

def handle_webhook(request, _settings):
    bot.set_token(_settings.token)
    bot.set_settings(_settings)
    bot.process_new_updates([telebot.types.Update.de_json(request.body.decode("utf-8"))])


def handle_longpoll(_settings):
    bot.set_token(_settings.token)
    bot.set_settings(_settings)
    bot.infinity_polling()

def get_user_id(message):
    return message.from_user.id

def delete_inline_markup(user_id, call_message):
    return bot.delete_message(user_id, call_message)


@bot.message_handler(commands=['start'])
def start(message):
    markup = Markups()
    bot.send_message(get_user_id(message), markup.texts.text_start, reply_markup=markup.main_menu, parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: True)
def menu_callback(call):
    
    markups = Markups()
    delete_message = True

    # Главное меню
    if call.data == "about":
        bot.send_message(call.from_user.id, markups.texts.text_about, reply_markup=markups.about_menu(bot.settings.contact_us), parse_mode='Markdown')
    
    elif call.data == "main_bunt":
        bot.send_message(call.from_user.id, markups.texts.text_bunt, reply_markup=markups.about_bunt(bot.settings.free_channel_url), parse_mode='Markdown')
        
    elif call.data == "main_prich":
        delete_message = False
   
    elif call.data == "channel_bunt":
        delete_message = False

    # Меню about
    elif call.data == "price":
        user = TelegramUser.objects.filter(user_id=call.from_user.id).first()
        bot.send_message(call.from_user.id, markups.texts.text_price, reply_markup=markups.subscribe_menu(user), parse_mode='Markdown')
    
    elif call.data == "contact_us":
        delete_message = False
    
    elif call.data == "main_menu":
        bot.send_message(call.from_user.id, markups.texts.text_start, reply_markup=markups.main_menu, parse_mode='Markdown')
    
    # Меню подписки
    elif call.data == "subscribe":
        user, _ = TelegramUser.objects.get_or_create(
            user_id = call.from_user.id
        )
        
        bot.send_message(call.from_user.id, markups.texts.text_pay, reply_markup=markups.pay_menu("google.com"), parse_mode="Markdown")


    elif call.data == "unsubscribe":
        bot.send_message(call.from_user.id, markups.texts.text_pay, reply_markup=markups.pay_menu("yandex.ru"), parse_mode="Markdown")
    
    elif call.data == "offerta":
        bot.send_document(call.from_user.id, bot.settings.offerta)
        bot.answer_callback_query(call.id)
        delete_message = False
    
    elif call.data == "policy":
        bot.send_document(call.from_user.id, bot.settings.policy)
        bot.answer_callback_query(call.id)
        delete_message = False
    
    # Меню оплаты
    elif call.data == "pay":
        bot.send_message(call.from_user.id, markups.texts.text_after_pay, parse_mode='Markdown')

    if not delete_message:
        return
    
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as e:
        print(e)