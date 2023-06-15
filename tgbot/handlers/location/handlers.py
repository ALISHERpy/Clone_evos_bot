import telegram
from telegram import Update
from telegram.ext import CallbackContext

from tgbot.handlers.location.static_text import share_location, thanks_for_location
from tgbot.handlers.location.keyboards import send_location_keyboard,yes_or_no
from users.models import User, Location
from tgbot.handlers.menu.find_distance import calculate_driving_distance as get_distance ,get_distance_name


def ask_for_location(update: Update, context: CallbackContext) -> None:
    """ Entered /ask_location command"""
    u = User.get_user(update, context)

    context.bot.send_message(
        chat_id=u.user_id,
        text=share_location,
        reply_markup=send_location_keyboard()
    )


def location_handler(update: Update, context: CallbackContext) -> None:
    # receiving user's location
    u = User.get_user(update, context)
    lat, lon = update.message.location.latitude, update.message.location.longitude
    # by ALI
    name_distance= get_distance_name(lat, lon)
    
    Location.objects.create(user=u, latitude=lat, longitude=lon)

    # BY ALI
    my_latitude = 41.35313914241534 
    my_longitude = 69.28806543775883  

    user_latitude = lat
    user_longitude = lon
    

    distance = get_distance(my_latitude, my_longitude, user_latitude, user_longitude)
    distance=distance/1000
    distance = f"{distance:.3f}"

    if distance is not None:
        update.message.reply_text(f"{distance} km uzoqlikda.")
        update.message.reply_text(f"manzil : {name_distance}\nBu siz yuborgan manzilinggizmi?",reply_markup=yes_or_no())
    else:
        update.message.reply_text("Yuboriligan location bo'yicha xatolik...")
    