from telebot import types
from telegramBot.models import BotDictionary, TelegramUser

class Markups:
    def __init__(self):
        self._dict = BotDictionary.objects.first()
    


    @property
    def texts(self):
        return self._dict

    @property
    def main_menu(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row_width = 1

        keyboard.add(
            types.InlineKeyboardButton(self._dict.btn_process, callback_data='about'),
            types.InlineKeyboardButton(self._dict.btn_bunt, callback_data='main_bunt'),
            #types.InlineKeyboardButton(self._dict.btn_prichess, callback_data='main_prich')
            )

        return keyboard
    
    def about_menu(self, contact_us_url: str):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row_width = 1

        keyboard.add(
            types.InlineKeyboardButton(self._dict.btn_price, callback_data='price'),
            types.InlineKeyboardButton(self._dict.btn_contact, callback_data='contact_us', url=contact_us_url),
            types.InlineKeyboardButton(self._dict.btn_menu, callback_data='main_menu')
        )

        return keyboard
    
    def subscribe_menu(self, user: TelegramUser):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row_width = 1

        btn_sub_or_unsub = types.InlineKeyboardButton(self._dict.btn_subscribe, callback_data='subscribe')

        if user is not None:
            if user.subscription is not None and user.auto_payment:
                btn_sub_or_unsub = types.InlineKeyboardButton(self._dict.btn_subscribe, callback_data='unsubscribe')


        keyboard.add(
            btn_sub_or_unsub,
            types.InlineKeyboardButton(self._dict.btn_offerta, callback_data='offerta'),
            types.InlineKeyboardButton(self._dict.btn_policy, callback_data='policy'),
            types.InlineKeyboardButton(self._dict.btn_back, callback_data='about')
        )

        return keyboard
    

    def pay_menu(self, generate_link: str):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row_width = 1

        keyboard.add(
            types.InlineKeyboardButton(self._dict.btn_pay, callback_data='pay', url=generate_link),
            types.InlineKeyboardButton(self._dict.btn_back, callback_data='price')
        )

        return keyboard


    def about_bunt(self, channel_url: str ):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row_width = 1

        keyboard.add(
            types.InlineKeyboardButton(self._dict.btn_bunt_channel, callback_data='channel_bunt', url=channel_url),
            types.InlineKeyboardButton(self._dict.btn_menu, callback_data='main_menu')
        )

        return keyboard
