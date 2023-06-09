
import logging
from typing import Dict
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton, Contact
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

REG, NAME, SURNAME, CONTACT = range(4)

TOKEN = "5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04"

reply_keyboard = [
    [
        KeyboardButton(text="Registration"),
    ]
]

markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,input_field_placeholder="\"Registration\"ni bosing")

reply_keyboard = [
    [
        KeyboardButton(text="SHARE CONTACT", request_contact=True),
    ]
]

mark_up = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)

def get_data(user_data: Dict[str, str]) -> None:

    facts = [f'{key} {value}' for key, value in user_data.items()]
    
    return "\n".join(facts).join(['\n', '\n'])

def start(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text('Salom, iltimos registraciyadan oting', reply_markup=markup)
    
    text = update.message.text

    return REG

def reg(update: Update, context: CallbackContext) -> None:

    update.message.reply_text('Ismingizni kiriting')
    
    return NAME


def name(update: Update, context: CallbackContext) -> None:
    
    text = update.message.text
    
    context.user_data["Ismingiz : "] = text
    
    update.message.reply_text(text='Familiyangizni kiriting')

    return SURNAME

def surname(update: Update, context: CallbackContext) -> None:
    
    text = update.message.text
    
    context.user_data["Familyangiz : "] = text
    
    update.message.reply_text("Place share your contact", reply_markup=mark_up)

    return CONTACT

def contact(update: Update, context: CallbackContext) -> None:

    kontakt = update.message.contact.phone_number

    context.user_data["Telefon raqamingiz : "] = kontakt

    user_data = context.user_data

    update.message.reply_text(
        f"Malumotlar: {get_data(user_data)}Ko\'rishguncha !", reply_markup=ReplyKeyboardRemove(),
    )
    
    return ConversationHandler.END


def done(update: Update, context: CallbackContext) -> None:
    pass
    

def main() -> None:

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            REG: [
                MessageHandler(
                    Filters.regex('^Registration$'), reg
                ),
            ],
            NAME: [ 
                MessageHandler(
                    Filters.text, name
                ),
            ],
            SURNAME: [
                MessageHandler(
                    Filters.text, surname
                )
            ],
            CONTACT: [
                MessageHandler(
                    Filters.contact, contact
                )
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()