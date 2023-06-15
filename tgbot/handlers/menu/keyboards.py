from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from tgbot.handlers.menu import static_text as menu_text 
from product.models import Category

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
            KeyboardButton(text=menu_text.address_send_location),
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
    types = Category.objects.all()
    n = len(types)
    if n % 2 == 0:
        buttons = [
            [ 
                KeyboardButton(text=types[number].name), 
                KeyboardButton(text=types[number+1].name),
            ] for number in range(0, n, 2)
        ]
        buttons.append([ KeyboardButton(text=menu_text.back) ])
    else:
        buttons = [
            [ 
                KeyboardButton(text=types[number].name), 
                KeyboardButton(text=types[number+1].name) 
            ] for number in range(0, n - 1, 2)
        ]
        buttons.append([ KeyboardButton(text=types[n - 1].name) ])
        buttons.append([ KeyboardButton(text=menu_text.back) ])

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

def comment_get_contact() -> ReplyKeyboardMarkup:
    buttons = [
        [ KeyboardButton(text=menu_text.comment_contact, request_contact=True), ],
        [ KeyboardButton(text=menu_text.back) ],
    ]
        
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

def get_back() -> ReplyKeyboardMarkup:
    buttons = [
        [ KeyboardButton(text=menu_text.back), ],
    ]
        
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
 

