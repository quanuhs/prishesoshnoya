import telebot
from telebot import types
from . import texts, markups, text_buttons

from ..models import BotDictionary



class TelegramBot(telebot.TeleBot):
    settings = None
    
    def set_token(self, new_token):
        self.token = new_token
    
    def set_settings(self, settings):
        self.settings = settings


bot: TelegramBot = TelegramBot(None)

def handle(request, _settings):
    bot.set_token(_settings.token)
    bot.set_settings(_settings)
    bot.process_new_updates([telebot.types.Update.de_json(request.body.decode("utf-8"))])


def get_user_id(message):
    return message.from_user.id

def delete_inline_markup(user_id, call_message):
    return bot.delete_message(user_id, call_message)


def generate_markup(buttons):
    menu = types.InlineKeyboardMarkup()
    menu.row_width = 1
    for button in buttons:
        menu.add(types.InlineKeyboardButton(button.title, callback_data={"button_id": button.id}))
    return menu

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(get_user_id(message), texts.start_text,  reply_markup=markups.main_menu2, parse_mode='Markdown')
    bot.send_message(get_user_id(message), texts.choice_start_text, parse_mode='Markdown')


# @bot.callback_query_handler(func=lambda call: True)
# def handle_callback(call):
#     # Получаем id кнопки из call
#     button_id = call.data.get("button_id")

#     if button_id:
#         BotButton.objects.
        

class Markups:
    def __init__(self, bot_dictionary):
        self.bot_dictionary = bot_dictionary
    
    @property
    def main_process(self):
        return []



@bot.callback_query_handler(func=lambda call: True)
def menu_callback(call):
    bot_dictionary = BotDictionary.objects.first()

    if bot_dictionary is None:
        return
    
    
    
    # Главное меню
    if call.data == "main_process":
        bot.send_message(call.from_user.id, texts.about_text, reply_markup=markups.about_menu2, parse_mode='Markdown')
    
    elif call.data == "main_bunt":
        bot.send_message(call.from_user.id, texts.about_bunt, reply_markup=markups.about_bunt2, parse_mode='Markdown')
    
    elif call.data == "main_prich":
        pass
   
    elif call.data == "channel_bunt":
        pass
    
    
    # Меню about
    elif call.data == "price_ques":
        bot.send_message(call.from_user.id, texts.price_text, reply_markup=markups.subs_menu2, parse_mode='Markdown')
    
    elif call.data == "write_us":
        pass
    
    elif call.data == "back_main_menu":
        bot.send_message(call.from_user.id, texts.start_text, reply_markup=markups.main_menu2, parse_mode='Markdown')
    
    
    # Меню подписки
    elif call.data == "subscribe":
        bot.send_message(call.from_user.id, texts.subscribe_text, reply_markup=markups.pay_menu2, parse_mode="html")
    
    elif call.data == "offerta":
        pass
    
    elif call.data == "politics":
        pass
    
    elif call.data == "back_about":
        bot.send_message(call.from_user.id, texts.about_text, reply_markup=markups.about_menu2, parse_mode='Markdown')

    
    # Меню оплаты
    elif call.data == "pay":
        bot.send_message(call.from_user.id, texts.after_pay_text, parse_mode='html')

    elif call.data == "back_subs":
        bot.send_message(call.from_user.id, texts.price_text, reply_markup=markups.subs_menu2, parse_mode='Markdown')


    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as e:
        print(e)