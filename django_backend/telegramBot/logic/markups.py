from telebot import types
from . import text_buttons


# Главное меню
main_menu2 = types.InlineKeyboardMarkup()
main_menu2.row_width = 1
main_menu2.add(types.InlineKeyboardButton(text_buttons.about_process_button, callback_data='main_process'),
               types.InlineKeyboardButton(text_buttons.about_bunt_button, callback_data='main_bunt'),
               types.InlineKeyboardButton(text_buttons.about_prich_button, callback_data='main_prich'))


# Меню about
about_menu2 = types.InlineKeyboardMarkup()
about_menu2.row_width = 1
about_menu2.add(types.InlineKeyboardButton(text_buttons.price_ques_button, callback_data='price_ques'),
               types.InlineKeyboardButton(text_buttons.write_us_button, callback_data='write_us'),
               types.InlineKeyboardButton(text_buttons.back_to_start_button, callback_data='back_main_menu'))


# Меню подписки
subs_menu2 = types.InlineKeyboardMarkup()
subs_menu2.row_width = 1
subs_menu2.add(types.InlineKeyboardButton(text_buttons.subscribe_button, callback_data='subscribe'),
               types.InlineKeyboardButton(text_buttons.offerta_button, callback_data='offerta'),
               types.InlineKeyboardButton(text_buttons.politcs_button, callback_data='politics'),
               types.InlineKeyboardButton(text_buttons.back_about_menu_button, callback_data='back_about'))


# Меню оплаты
pay_menu2 = types.InlineKeyboardMarkup()
pay_menu2.row_width = 1
pay_menu2.add(types.InlineKeyboardButton(text_buttons.pay_button, callback_data='pay', url="https://google.com"),
               types.InlineKeyboardButton(text_buttons.back_subs_menu_button, callback_data='back_subs'))


# Меню about bunt
about_bunt2 = types.InlineKeyboardMarkup()
about_bunt2.row_width = 1
about_bunt2.add(types.InlineKeyboardButton(text_buttons.channel_bunt_button, callback_data='channel_bunt', url=""),
               types.InlineKeyboardButton(text_buttons.back_to_start_button, callback_data='back_main_menu'))

