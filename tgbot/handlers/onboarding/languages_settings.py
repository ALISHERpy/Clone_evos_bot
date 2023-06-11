
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton, Contact
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

from tgbot.handlers.onboarding.handlers import reply_keyboards as bosh_sahifa_tugma
ortgaaa = [['⬅️ Ortga']]
reply_keyboard1=[["Tilni o'zgartirish" ],["⬅️ Ortga"]]
lg_kb=[["🇺🇿 O'zbekcha"],["🇷🇺 Русский"]]




GET_LANGUAGE, HAVE_DONE= range(2)

def get_start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Harakat tanlang:",reply_markup=ReplyKeyboardMarkup(
            reply_keyboard1, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    return GET_LANGUAGE



def get_lg(update: Update, context: CallbackContext) -> int:
    
    user = update.message.from_user
    if update.message.text =="⬅️ Ortga":
        update.message.reply_text(f"Bosh sahifa " ,reply_markup=ReplyKeyboardMarkup(
            bosh_sahifa_tugma, one_time_keyboard=True, resize_keyboard=True
        ),)
        return ConversationHandler.END
    else:
        update.message.reply_text("Tilni tanlang:",reply_markup=ReplyKeyboardMarkup(
            lg_kb,resize_keyboard=True),)
        

    return HAVE_DONE

def have_done(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(f"✅ Tayyor !",reply_markup=ReplyKeyboardMarkup(
            bosh_sahifa_tugma, one_time_keyboard=True, resize_keyboard=True),)
        
    return ConversationHandler.END


def get_back(update: Update, context: CallbackContext) -> int:
        
    update.message.reply_text(f"Bosh sahifa " ,reply_markup=ReplyKeyboardMarkup(
            bosh_sahifa_tugma, one_time_keyboard=True, resize_keyboard=True
        ),)

    
    return ConversationHandler.END