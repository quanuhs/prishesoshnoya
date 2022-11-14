import telebot
from telebot import types
from . import texts, text_buttons

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


@bot.message_handler(commands=['start'])
def start(message):
    markup = Markups()
    bot.send_message(get_user_id(message), texts.start_text,  reply_markup=markup.main_menu, parse_mode='Markdown')
    bot.send_message(get_user_id(message), texts.choice_start_text, parse_mode='Markdown')


class Markups:
    def __init__(self):
        self._dict = BotDictionary.objects.first()
    

    @property
    def main_menu(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row_width = 1

        keyboard.add(
            types.InlineKeyboardButton(self._dict.btn_process, callback_data='main_process'),
            types.InlineKeyboardButton(self._dict.btn_bunt, callback_data='main_bunt'),
            types.InlineKeyboardButton(self._dict.btn_prichess, callback_data='main_prich')
            )

        return keyboard
    
    @property
    def about_menu(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row_width = 1

        keyboard.add(
            types.InlineKeyboardButton(self._dict.btn_price, callback_data='price_ques'),
            types.InlineKeyboardButton(self._dict.btn_contact, callback_data='write_us'),
            types.InlineKeyboardButton(self._dict.btn_menu, callback_data='back_main_menu')
        )

        return keyboard
    
    @property
    def subscribe_menu(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row_width = 1

        keyboard.add(
            types.InlineKeyboardButton(self._dict.btn_subscribe, callback_data='subscribe'),
            types.InlineKeyboardButton(self._dict.btn_offerta, callback_data='offerta'),
            types.InlineKeyboardButton(self._dict.btn_politics, callback_data='politics'),
            types.InlineKeyboardButton(self._dict.btn_back, callback_data='back_about')
        )

        return keyboard
    

    @property
    def pay_menu(self, generate_link):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row_width = 1

        keyboard.add(
            types.InlineKeyboardButton(self._dict.btn_pay, callback_data='pay', url=generate_link),
            types.InlineKeyboardButton(self._dict.btn_back, callback_data='back_subs')
        )

        return keyboard


    @property
    def about_bunt(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row_width = 1

        keyboard.add(
            types.InlineKeyboardButton(self._dict.btn_bunt_channel, callback_data='channel_bunt', url=""),
            types.InlineKeyboardButton(self._dict.btn_menu, callback_data='back_main_menu')
        )

        return keyboard


@bot.callback_query_handler(func=lambda call: True)
def menu_callback(call):
    
    markups = Markups()
    
    # Главное меню
    if call.data == "main_process":
        bot.send_message(call.from_user.id, texts.about_text, reply_markup=markups.about_menu, parse_mode='Markdown')
    
    elif call.data == "main_bunt":
        bot.send_message(call.from_user.id, texts.about_bunt, reply_markup=markups.about_bunt, parse_mode='Markdown')
    
    elif call.data == "main_prich":
        pass
   
    elif call.data == "channel_bunt":
        pass


    # Меню about
    elif call.data == "price_ques":
        bot.send_message(call.from_user.id, texts.price_text, reply_markup=markups.subscribe_menu, parse_mode='Markdown')
    
    elif call.data == "write_us":
        pass
    
    elif call.data == "back_main_menu":
        bot.send_message(call.from_user.id, texts.start_text, reply_markup=markups.main_menu, parse_mode='Markdown')
    
    
    # Меню подписки
    elif call.data == "subscribe":
        bot.send_message(call.from_user.id, texts.subscribe_text, reply_markup=markups.pay_menu, parse_mode="html")
    
    elif call.data == "offerta":
        pass
    
    elif call.data == "politics":
        pass
    
    elif call.data == "back_about":
        bot.send_message(call.from_user.id, texts.about_text, reply_markup=markups.about_menu, parse_mode='Markdown')

    
    # Меню оплаты
    elif call.data == "pay":
        bot.send_message(call.from_user.id, texts.after_pay_text, parse_mode='html')

    elif call.data == "back_subs":
        bot.send_message(call.from_user.id, texts.price_text, reply_markup=markups.subscribe_menu, parse_mode='Markdown')

    try:
        
        bot.delete_message(call.message.chat.id, call.message.message_id)
    
    except Exception as e:
        print(e)