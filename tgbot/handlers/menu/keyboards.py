from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from tgbot.handlers.menu import static_text as menu_text 
from product.models import Category, Product

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

def address_list(objs) -> ReplyKeyboardMarkup:

    types=objs
    n = len(types)
    if n % 2 == 0:
        buttons = [
            [ 
                KeyboardButton(text=types[number].distanations), 
                KeyboardButton(text=types[number+1].distanations),
            ] for number in range(0, n, 2)
        ]
        buttons.append([ KeyboardButton(text=menu_text.back) ])
    else:
        buttons = [
            [ 
                KeyboardButton(text=types[number].distanations), 
                KeyboardButton(text=types[number+1].distanations) 
            ] for number in range(0, n - 1, 2)
        ]
        buttons.append([ KeyboardButton(text=types[n - 1].distanations) ])
        buttons.append([ KeyboardButton(text=menu_text.back) ])


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

def product_list(letter: str) -> ReplyKeyboardMarkup:
    products = Product.objects.filter(category__name=letter, parent=None)
    n = len(products)
    if n == 0:
        buttons = [[ KeyboardButton(text=menu_text.back) ]]
    elif n % 2 == 0:
        buttons = [
            [ 
                KeyboardButton(text=products[number].name), 
                KeyboardButton(text=products[number+1].name),
            ] for number in range(0, n, 2)
        ]
        buttons.append([ KeyboardButton(text=menu_text.back) ])
    else:
        buttons = [
            [ 
                KeyboardButton(text=products[number].name), 
                KeyboardButton(text=products[number+1].name) 
            ] for number in range(0, n - 1, 2)
        ]
        buttons.append([ KeyboardButton(text=products[n - 1].name) ])
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

