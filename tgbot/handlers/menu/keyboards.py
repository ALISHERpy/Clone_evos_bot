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
        [ KeyboardButton(text=menu_text.address_my_addresses), ],
        [
            KeyboardButton(text=menu_text.address_send_location,request_location=True),
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

def category_list() -> ReplyKeyboardMarkup:
    buttons = [
        [ KeyboardButton(text="Lavash"), KeyboardButton(text="Burger"), ],
        [ KeyboardButton(text="Shaurma"), KeyboardButton(text="Sub"), ],
        [ KeyboardButton(text="Hot dog"), KeyboardButton(text=menu_text.back), ],
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
 

def choose_lg() -> ReplyKeyboardMarkup:
    x=menu_text.languages_key.split(',')

    buttons = [
        [ KeyboardButton(text=x[0]), ],
        [ KeyboardButton(text=x[1]), ],
    ]  
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
 
def entry_lg() -> ReplyKeyboardMarkup:
    buttons = [
        [ KeyboardButton(text=menu_text.entry_language), ],
        [ KeyboardButton(text=menu_text.back), ],
    ]
        
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

