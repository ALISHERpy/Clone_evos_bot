import telegram
from telegram import Update
from telegram.ext import CallbackContext

from tgbot.handlers.location.static_text import share_location, thanks_for_location
from tgbot.handlers.location.keyboards import send_location_keyboard, yes_or_no
from users.models import User, Location
from tgbot.handlers.menu.find_distance import calculate_driving_distance as get_distance, get_distance_name
from django.http import HttpResponse
from tgbot.states import *

    
def location_handler(update: Update, context: CallbackContext) -> None:
    # receiving user's location
    u = User.get_user(update, context)
    lat, lon = update.message.location.latitude, update.message.location.longitude
    
    name_distance= get_distance_name(lat, lon)

    my_latitude = 41.35313914241534 
    my_longitude = 69.28806543775883  

    user_latitude = lat
    user_longitude = lon
    

    distance = get_distance(my_latitude, my_longitude, user_latitude, user_longitude)
    distance=distance/1000
    distance = f"{distance:.3f}"

    if distance is not None:
        shipment_fee = (distance-15)*2000
        update.message.reply_text(f"<b>Masofa</b>: {distance} km.\n\n<b>Manzil</b> : {name_distance}\n<b>Yitkazib berish</b>: {shipment_fee} so'm!",parse_mode='HTML')
        update.message.reply_text("Bu siz yuborgan manzilinggizmi?",reply_markup=yes_or_no())
        context.user_data['manzil'] = name_distance
        context.user_data['shipment'] = shipment_fee
        return LOCATION_CONFIRM
    else:
        update.message.reply_text("Yuboriligan location bo'yicha xatolik...")
        return CHOOSE 
