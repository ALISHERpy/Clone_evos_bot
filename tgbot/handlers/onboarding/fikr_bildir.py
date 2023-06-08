
import logging
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

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

GET_CONTACT, GET_SUGGETIONS= range(2)


def boshlaa(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [
    [
        KeyboardButton(text="SHARE CONTACT", request_contact=True),
    ]
]

    update.message.reply_text("Cantact yuboring...",reply_markup=ReplyKeyboardMarkup(
            reply_keyboard),
    )

    return GET_CONTACT


def for_contact(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['⬅️ Ortga']]
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        'Fikringgizni yozib qoldiring...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),)
    

    return GET_SUGGETIONS


def for_suggestion(update: Update, context: CallbackContext) -> int:
    """Stores the photo and asks for a location."""
    user = update.message.from_user
    
    update.message.reply_text(f"{user.first_name} Fikr-mulohazangiz uchun rahmat " )

    update.message.reply_text(f"Bosh sahifa " ,reply_markup=ReplyKeyboardMarkup(
            bosh_sahifa_tugma, one_time_keyboard=True, resize_keyboard=True
        ),)

    return ConversationHandler.END




def for_ortga(update: Update, context: CallbackContext) -> int:
    """Stores the photo and asks for a location."""
    # user = update.message.from_user
    
    update.message.reply_text(f"Bosh sahifa " ,reply_markup=ReplyKeyboardMarkup(
            bosh_sahifa_tugma, one_time_keyboard=True, resize_keyboard=True
        ),)

    
    return ConversationHandler.END



    
