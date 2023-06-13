from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from tgbot.handlers.menu import static_text as menu_text 


def home_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [ KeyboardButton(text=menu_text.home_menu), ],
        [ KeyboardButton(text=menu_text.home_my_orders), ],
        [
            KeyboardButton(text=menu_text.home_comment),
            KeyboardButton(text=menu_text.home_settings),
        ],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

def menu_click_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [ KeyboardButton(text=menu_text.home_my_addresses), ],
        [
            KeyboardButton(text=menu_text.home_send_location),
            KeyboardButton(text=menu_text.back),
        ],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

def address_list() -> ReplyKeyboardMarkup:
    buttons = [
        [ KeyboardButton(text="Chilonzor"), ],
        [ KeyboardButton(text="Yunusobod"), ],
        [ KeyboardButton(text=menu_text.back), ],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

def comment_get_contact() -> ReplyKeyboardMarkup:
    buttons = [
        [ KeyboardButton(text=menu_text.comment_contact, request_contact=True), ],
        [ KeyboardButton(text=menu_text.back), ],
    ]
        
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

def get_back() -> ReplyKeyboardMarkup:
    buttons = [
        [ KeyboardButton(text=menu_text.back), ],
    ]
        
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
 

