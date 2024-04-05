from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
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

def category_list(let=None) -> ReplyKeyboardMarkup:
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

    if let == "basket":
        buttons.insert(0, [ KeyboardButton(text=menu_text.show_basket) ])
        
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

def prices_inline(obj: Product, num: int) -> InlineKeyboardMarkup:
    if num == 1:
        buttons = [
            [ InlineKeyboardButton(text=f"{obj.name} {obj.price}", callback_data=f'{obj.name}') ],
        ]
    elif num == 2:
        obj = obj.children.all()
        buttons = [
            [ 
                InlineKeyboardButton(text=f"{obj[0].name} {obj[0].price}", callback_data=f'{obj[0].name}'),
                InlineKeyboardButton(text=f"{obj[1].name} {obj[1].price}", callback_data=f'{obj[1].name}'),
            ],
        ]
    else:
        buttons = [
            [ InlineKeyboardButton(text="Wrong", callback_data="Wrong") ],
        ]

    return InlineKeyboardMarkup(buttons)

def plus_or_minus(num: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="-", callback_data="-"),
            InlineKeyboardButton(text=str(num), callback_data=f"{str(num)}"),
            InlineKeyboardButton(text="+", callback_data="+"),
        ],
        [
            InlineKeyboardButton(text="Savatga qo\'shish", callback_data="basket")
        ],
    ]

    return InlineKeyboardMarkup(buttons)

def savat_inline() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=menu_text.order_conf, callback_data="order_confirmed"),
        ],
        [   
            InlineKeyboardButton(text=menu_text.delete_basket, callback_data="basket_deleted"),
            InlineKeyboardButton(text=menu_text.back, callback_data="back"),
        ],
    ]

    return InlineKeyboardMarkup(buttons)

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
    x = menu_text.languages_key.split(',')

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


