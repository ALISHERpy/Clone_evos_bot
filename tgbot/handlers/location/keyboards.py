from telegram import ReplyKeyboardMarkup, KeyboardButton

from tgbot.handlers.location import static_text as locations_text
from tgbot.handlers.menu.static_text import back


def send_location_keyboard() -> ReplyKeyboardMarkup:
    # resize_keyboard=False will make this button appear on half screen (become very large).
    # Likely, it will increase click conversion but may decrease UX quality.
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=locations_text.SEND_LOCATION, request_location=True)]],
        resize_keyboard=True
    )

def yes_or_no() -> ReplyKeyboardMarkup:
    buttons = [
        [ KeyboardButton(text=locations_text.yes),KeyboardButton(text=locations_text.no), ],
         [ KeyboardButton(text=back)]
        
    ]    
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
