from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from tgbot.handlers.menu import static_text
from tgbot.handlers.menu import keyboards as menu_keyboard
# from tgbot.handlers.menu import static_text as menu_
# from tgbot.handlers.utils.info import extract_user_data_from_update
from users.models import User
# from tgbot.handlers.menu.keyboards import 
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton, Contact
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update

HOME, MENU, MY_ORDERS, COMMENT, SETTINGS = map(chr, range(8))
MY_ADDRESSES, SEND_LOCATION, ADDRESSES_LIST, = map(chr, range(8, 11))
CATEGORY_LIST, TYPE_OF_LIST, NUMBER_OF_PRODUCKT = map(chr, range(11, 14))
#  = map(chr, range(8))

def home_page(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Quyidagilardan birini tanlang", reply_markup=menu_keyboard.home_keyboard())

    return HOME

def click_menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="📍 Geolokatsiyani yuboring yoki yetkazib berish manzilini tanlang", reply_markup=menu_keyboard.menu_click_keyboard())

    return MENU

def my_orders(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="....Jami: 134 000 sum",)

def comment(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Fikringizni yuboring", reply_markup=menu_keyboard.())

def settings(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="", reply_markup=menu_keyboard.())

def address_list(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Yetkazib berish manzilni tanlang", reply_markup=menu_keyboard.address_list())

    return ADDRESSES_LIST

def category_list(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="", reply_markup=menu_keyboard.())



# def send_location(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="Manzil qabul qilindi", reply_markup=menu_keyboard.#())

def (update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="", reply_markup=menu_keyboard.())

# def (update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="", reply_markup=())