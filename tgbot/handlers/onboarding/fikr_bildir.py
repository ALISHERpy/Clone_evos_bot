
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

from dtb.settings import ADMINS
ADMINS=str(ADMINS)
ADMINS=ADMINS.split(",")
from users.models import User as Foydalanuvchilar





GET_CONTACT, GET_SUGGETIONS= range(2)


def boshlaa(update: Update, context: CallbackContext) -> int:
    
    user = update.message.from_user
    reply_keyboard = [
    [
        KeyboardButton(text="📞Mening raqamim", request_contact=True),
    ] ]

    #  tekshirish bor yo yuuu
    u=Foydalanuvchilar.objects.get(user_id=user.id)
    if u.contact_number:       
        update.message.reply_text(
        'Fikringgizni yozib qoldiring...',
        reply_markup=ReplyKeyboardMarkup(
            ortgaaa, one_time_keyboard=True, resize_keyboard=True
        ),)
        return GET_SUGGETIONS
        #  tekshirish bor yo yuuu


    update.message.reply_text("Siz bilan keyingi muloqot uchun kontaktni yuboring...",reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,resize_keyboard=True),
    )
    
    return GET_CONTACT


def for_contact(update: Update, context: CallbackContext) -> int:
    
    user = update.message.from_user
##### user's number set into database  by ALI
    contact_number = update.message.contact["phone_number"]
    user_obj = Foydalanuvchilar.objects.get(user_id=user.id)
    user_obj.contact_number = contact_number
    user_obj.save()

    if update.message.text=="⬅️ Ortga":
        update.message.reply_text(f"Bosh sahifa " ,reply_markup=ReplyKeyboardMarkup(
            bosh_sahifa_tugma, one_time_keyboard=True, resize_keyboard=True
        ),)
        return ConversationHandler.END
    
    
    update.message.reply_text(
        'Fikringgizni yozib qoldiring...',
        reply_markup=ReplyKeyboardMarkup(
            ortgaaa, one_time_keyboard=True, resize_keyboard=True
        ),)
    
    ##kiyingi state uchun data
    # context.user_data['number'] = contact_number
    return GET_SUGGETIONS


def for_suggestion(update: Update, context: CallbackContext) -> int:
        #eskidan olish
    # number = context.user_data['number'] 

    user = update.message.from_user
    
    if update.message.text=="⬅️ Ortga":
        update.message.reply_text(f"Bosh sahifa " ,reply_markup=ReplyKeyboardMarkup(
            bosh_sahifa_tugma, one_time_keyboard=True, resize_keyboard=True
        ),)
        

    else:
        number=Foydalanuvchilar.objects.get(user_id=user.id)   
        number=number.contact_number

        for user_id in ADMINS:
            context.bot.send_message(chat_id=user_id, text=f"""
            USER:  {user.full_name}\n@{user.username}\nCell phone: {number}

            💬xabar yubordi👇🏻:
            
            {update.message.text}
            """)
     
        update.message.reply_text(f"{user.first_name} Fikr-mulohazangiz uchun rahmat " ,reply_markup=ReplyKeyboardMarkup(
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



    
