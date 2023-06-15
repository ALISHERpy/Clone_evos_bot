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
    
HOME, CHOOSE, MENU, MY_ORDERS, COMMENT, SETTINGS = map(chr, range(6))
MY_ADDRESSES, SEND_LOCATION, ADDRESSES_LIST, = map(chr, range(6, 9))
CATEGORY_LIST, TYPE_OF_LIST, NUMBER_OF_PRODUCKT = map(chr, range(9, 12))
WRITE_COMMENT,COMMENT_DONE = map(chr, range(12, 14))
GET_LANGUAGE, HAVE_DONE= map(chr, range(14, 16))
LOCATION_CONFIRM=map(chr,range(16,17))




#  = map(chr, range(8))
from dtb.settings import ADMINS
ADMINS=str(ADMINS)
ADMINS=ADMINS.split(",")
from users.models import User as BotUser
from users.models import Location

def home_page(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Quyidagilardan birini tanlang(func:home page)", 
                              reply_markup=menu_keyboard.home_keyboard())

    return CHOOSE

def click_menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="📍 Geolokatsiyani yuboring yoki yetkazib berish manzilini tanlang", 
                              reply_markup=menu_keyboard.menu_click_keyboard())

    return MENU

def my_orders(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="....Jami: 134 000 sum", reply_markup=menu_keyboard.get_back())

    # return /

# def settings(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="", reply_markup=menu_keyboard.())

def address_list(update: Update, context: CallbackContext) -> None:
    u = BotUser.get_user(update, context)

    objs = Location.objects.filter(user=u)

    update.message.reply_text(text="Yetkazib berish manzilni tanlang", reply_markup=menu_keyboard.address_list(objs=objs))

    return ADDRESSES_LIST

def category_list(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text(text="Bo'limni tanlang.", reply_markup=menu_keyboard.category_list())

    try:
        manzilimiz=context.user_data['manzil'] 
        if manzilimiz:
            u = BotUser.get_user(update, context)
            objs = Location.objects.filter(user=u,distanations=manzilimiz)
            if not objs:
                Location.objects.create(user=u, latitude=999, longitude=888,distanations=manzilimiz)
    except Exception as e:
        print(e)

        pass

    return TYPE_OF_LIST


# def (update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="", reply_markup=menu_keyboard.())

# def (update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="", reply_markup=())



# def settings(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="", reply_markup=menu_keyboard.())

# def address_list(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="Yetkazib berish manzilni tanlang", reply_markup=menu_keyboard.address_list())

#     return ADDRESSES_LIST

# def category_list(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="Bo'limni tanlang.", reply_markup=menu_keyboard.category_list())


# def (update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="", reply_markup=menu_keyboard.())

# def (update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="", reply_markup=menu_keyboard.())

# def (update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(text="", reply_markup=())



def comment(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    u=BotUser.objects.get(user_id=user.id)
    if u.contact_number:   
        update.message.reply_text(text="Fikringizni yuboring....", reply_markup=menu_keyboard.get_back())
        return COMMENT_DONE
    
    update.message.reply_text(text="Siz bilan keyingi muloqot uchun kontaktni yuboring...", 
    reply_markup=menu_keyboard.comment_get_contact())
    return WRITE_COMMENT

def write_comment(update: Update, context: CallbackContext) -> None:
    
#####set user's number  into database  by ALI
    user = update.message.from_user
    u=BotUser.objects.get(user_id=user.id)
    contact_number = update.message.contact["phone_number"]
    user_obj = BotUser.objects.get(user_id=user.id)
    user_obj.contact_number = contact_number
    user_obj.save()

    update.message.reply_text(text="Fikringizni yuboring....", 
    reply_markup=menu_keyboard.get_back())
    return COMMENT_DONE


def comment_done(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    #ortga bosganida
    if update.message.text==static_text.back:
        update.message.reply_text(f"Bosh sahifa ",
         reply_markup=menu_keyboard.home_keyboard())
    else:
        number=BotUser.objects.get(user_id=user.id)   
        number=number.contact_number

        for admin_id in ADMINS:
            context.bot.send_message(chat_id=admin_id, text=f"""
            USER:  {user.full_name}\n@{user.username}\nCell phone: {number}

            💬xabar yubordi👇🏻:
            
            {update.message.text}
            """)
     
        update.message.reply_text(f"{user.first_name} Fikr-mulohazangiz uchun rahmat " ,
         reply_markup=menu_keyboard.home_keyboard())
        
    return CHOOSE


    # LANGUAGES SETTINGS....
def settings(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Harakat tanlang:",
         reply_markup=menu_keyboard.entry_lg())
    
    return GET_LANGUAGE

def get_lg(update: Update, context: CallbackContext) -> int:
    
    user = update.message.from_user
    if update.message.text==static_text.back:
        update.message.reply_text(f"Bosh sahifa ",
         reply_markup=menu_keyboard.home_keyboard())
         
    else:
        update.message.reply_text("Tilni tanlang:",
        reply_markup=menu_keyboard.choose_lg())
        

    return HAVE_DONE

def have_done(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(f"✅ Tayyor !",
        reply_markup=menu_keyboard.home_keyboard())
        
    return CHOOSE

# def get_back(update: Update, context: CallbackContext) -> int:
        
#     update.message.reply_text(f"Bosh sahifa ",
#         reply_markup=menu_keyboard.home_keyboard())
    
#     # return ConversationHandler.END
