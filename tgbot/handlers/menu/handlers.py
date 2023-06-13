from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from tgbot.handlers.menu import static_text
from tgbot.handlers.menu.keyboards import home_keyboard, menu_click_keyboard
# from tgbot.handlers.utils.info import extract_user_data_from_update
from users.models import User
# from tgbot.handlers.menu.keyboards import 
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton, Contact
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update

HOME, MENU, MY_ORDERS, COMMENT, SETTINGS, MY_ADDRESSES, SEND_LOCATION, ADDRESSES_LIST, = range(8)

def home_page(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Quyidagilardan birini tanlang", reply_markup=home_keyboard())

def click_menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="📍 Geolokatsiyani yuboring yoki yetkazib berish manzilini tanlang", reply_markup=menu_click_keyboard())

def address_list(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Yetkazib berish manzilni tanlang", reply_markup=address_list())

# def send_location(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="Manzil qabul qilindi", reply_markup=())

def (update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="", reply_markup=())

# def (update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="", reply_markup=())