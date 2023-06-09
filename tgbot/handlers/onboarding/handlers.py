import datetime

from django.utils import timezone
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from tgbot.handlers.onboarding import static_text
from tgbot.handlers.utils.info import extract_user_data_from_update
from users.models import User
from tgbot.handlers.onboarding.keyboards import make_keyboard_for_start_command
#ALI
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton, Contact
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update

reply_keyboards = [['🍴 Menyu'],["🛍 Mening buyurtmalarim"],["✍️ Fikr bildirish","⚙️ Sozlamalar"]]

def command_start(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)
    #ALI
    
    #ALI
    if created:
        text = static_text.start_created.format(first_name=u.first_name)
    else:
        text = static_text.start_not_created.format(first_name=u.first_name)

    update.message.reply_text(text=text,
                              reply_markup=ReplyKeyboardMarkup(
            reply_keyboards, one_time_keyboard=True, input_field_placeholder='Bosh sahifa by Ali',resize_keyboard=True
        ),)
    
def None_of_them(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text("Quyidagilardan birini tanlang",
                              reply_markup=ReplyKeyboardMarkup(
            reply_keyboards, one_time_keyboard=True, input_field_placeholder='Bosh sahifa',resize_keyboard=True
        ),)


def secret_level(update: Update, context: CallbackContext) -> None:
    
    user_id = extract_user_data_from_update(update)['user_id']
    text = static_text.unlock_secret_room.format(
        user_count=User.objects.count(),
        active_24=User.objects.filter(updated_at__gte=timezone.now() - datetime.timedelta(hours=24)).count()
    )
    
    context.bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=update.callback_query.message.message_id,
        parse_mode=ParseMode.HTML
    )