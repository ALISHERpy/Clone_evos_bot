from telegram import ParseMode, Update
from telegram.ext import CallbackContext
from telegram import Bot

from tgbot.handlers.menu import static_text
from tgbot.handlers.menu import keyboards as menu_keyboard
from users.models import User
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton, Contact
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
    
from tgbot.states import *
from product.models import Product, Category,Basket


from dtb.settings import ADMINS
ADMINS=str(ADMINS)
ADMINS=ADMINS.split(",")

from users.models import User as BotUser
from users.models import Location


def home_page(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Quyidagilardan birini tanlang...", 
                              reply_markup=menu_keyboard.home_keyboard())

    return CHOOSE

def click_menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="📍 Geolokatsiyani yuboring yoki yetkazib berish manzilini tanlang", 
                              reply_markup=menu_keyboard.menu_click_keyboard())

    return MENU

def my_orders(update: Update, context: CallbackContext) -> None:

    user_name = update.message.from_user.username
    the_user = BotUser.objects.get(username=user_name)

    obj=Basket.objects.filter(user=the_user)[0]
    mahsulot=int(obj.count*float(obj.price)*1000)
    msg=f"<b>{obj.count}ta {obj.product}:</b> {mahsulot} sum\n"
    
    try:
        shipment_fee=str(context.user_data['shipment']) 
        msg=msg+ "<b>Yitkazib berish: <b/>" + shipment_fee + " sum"
        msg=msg+f"<b>\nHammasi bo'lib:</b> {float(shipment_fee) + mahsulot}"

    except Exception as err:
        # print(err)
        pass
        
    update.message.reply_text(text=msg, 
                              reply_markup=menu_keyboard.get_back(),parse_mode='HTML')

    # return /


def address_list(update: Update, context: CallbackContext) -> None:
    u = BotUser.get_user(update, context)

    objs = Location.objects.filter(user=u)

    update.message.reply_text(text="Yetkazib berish manzilni tanlang", 
                              reply_markup=menu_keyboard.address_list(objs=objs))
    
    return ADDRESSES_LIST

def category_list(update: Update, context: CallbackContext) -> None:


    try:
        manzilimiz=context.user_data['manzil'] 
        if manzilimiz:
            u = BotUser.get_user(update, context)
            objs = Location.objects.filter(user=u,distanations=manzilimiz)
            if not objs:
                Location.objects.create(user=u, latitude=121212, longitude=888,
                distanations=manzilimiz,shipment_cost=context.user_data['shipment'] )
    except Exception as e:
        pass
    
    
    if update.message.text not in ("✅HA","⬅️ Ortga"):
        context.user_data['manzil'] =update.message.text

    update.message.reply_text(text="Bo'limni tanlang.", 
                              reply_markup=menu_keyboard.category_list())
    
    return CATEGORY_LIST

def type_of_list(update: Update, context: CallbackContext) -> None:
    letter = update.message.text

    if Category.objects.filter(name=letter):
        update.message.reply_text(text="Tanlang", 
                                  reply_markup=menu_keyboard.product_list(letter=letter))

        return CHOOSE_BIG_OR_MINI
    else:
        update.message.reply_text(text="Something wrong!\nTry again, plase!", 
                                  reply_markup=menu_keyboard.category_list())

        return TYPE_OF_LIST

def choose_big_or_mini(update: Update, context: CallbackContext) -> None:
    letter = update.message.text
    obj = Product.objects.filter(parent=None, name=letter)[0]
    txt = f"{obj.name}: {obj.description}\nNarxi: {obj.price}.000 sum"
    if obj.children.all():
        update.message.reply_photo(photo=obj.photo,
                                  caption=txt,
                                  reply_markup=menu_keyboard.prices_inline(obj=obj, num=2))
    else:
        update.message.reply_photo(photo=obj.photo,
                                  caption=txt,
                                  reply_markup=menu_keyboard.prices_inline(obj=obj, num=1))
    
    return COUNT_OF_PRODUCT

def simple(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    # query.edit_message_reply_markup(reply_markup=menu_keyboard.plus_or_minus(num=number))
    context.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
    
    obj = Product.objects.filter(name=query.data)[0]
    context.bot.send_photo(chat_id=query.from_user.id, photo=obj.photo,
                           caption=f"{obj.name}: {obj.description}\nNarxi: {obj.price}", 
                           reply_markup=menu_keyboard.plus_or_minus(num=1))

    context.user_data['obj'] = obj.id

    return TEST

number = 1
def simple1(update: Update, context: CallbackContext) -> None:
    global number
    query = update.callback_query

    if query.data == '+':
        number += 1
        query.answer(text=f"{number} ta")
        query.edit_message_reply_markup(reply_markup=menu_keyboard.plus_or_minus(num=number))
    
    elif query.data == '-' and number != 1:        
        number -= 1
        query.answer(text=f"{number} ta")
        query.edit_message_reply_markup(reply_markup=menu_keyboard.plus_or_minus(num=number))
    
    elif query.data == 'basket':
        query.answer(text="Savatga qo'shildi✅")

        obj = Product.objects.get(id=context.user_data['obj'])

        user_name = query.from_user.username
        the_user = BotUser.objects.get(username=user_name)

        if not Basket.objects.filter(product=obj,user=the_user):
            Basket.objects.create(user=the_user, product=obj,
                                  count=number, price=obj.price)
        else:
            new_value = Basket.objects.filter(product=obj)[0].count + number
            Basket.objects.filter(product=obj).update(count=new_value)
            # print(f"\n\n\n\n{basket}\n\n\n")
            # new_value = basket.count + number
            # Basket.objects.filter(product=obj).update(count=new_value)
            
        context.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
        context.bot.send_message(chat_id=query.message.chat_id,
                                 text="Bo'limni tanlang.",
                                 reply_markup=menu_keyboard.category_list(let="basket"))
        
        return CATEGORY_LIST 
        
        # context.user_data['shipment'] 

    return TEST


# from telegram import InputMediaPhoto, InputMediaPhotoCaption

def show_basket(update: Update, context: CallbackContext) -> None:
    msg = "Savatda:\n"

    summm=0   
    for el in Basket.objects.filter(user__user_id=update.effective_user.id):
        x=el.count*float(el.product.price)*1000
        msg += f"{el.count}✖️{el.product.name}  {x} sum \n"
        summm+=x
    msg+=f"     <b>Jami: {summm}</b>"
    update.message.reply_text(text=msg,parse_mode="HTML",reply_markup=menu_keyboard.savat_inline())

    
    context.user_data['basket'] = update.effective_user.id

    return CATEGORY_LIST

def callback_basket(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    msg=''
    
    
    # print(query)

    if query.data=="back":
        query.answer(text="🔙")
        context.bot.send_message(chat_id=query.message.chat_id,
                                 text="Bo'limni tanlang.")
        context.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)                


    elif query.data=="basket_deleted":
        
        query.answer(text="🗑 ❌")
        Basket.objects.filter(user__user_id=context.user_data['basket']).delete()
        #tozalandi ....
        context.bot.send_message(chat_id=query.message.chat_id,
                                 text="Savatcha o'chirildi !\nBosh menyu:",reply_markup=menu_keyboard.home_keyboard())
        
        context.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
        return CHOOSE

    
    elif query.data== "order_confirmed":
        query.answer(text="✅")
        user=query.from_user
        

        msg=f"\n🆕Yangi buyurtma 👇🏻\n\n"\
            f"ism:  {user.full_name}\n" \
            f"username: @{user.username}\n" \

        try:
            number = BotUser.objects.get(user_id=context.user_data['basket'] )   
            number = number.contact_number
            msg+=f"Cell phone: +{number}\n\n" 
        except:
            pass
            

        summm=0
        for el in Basket.objects.filter(user__user_id=context.user_data['basket']):
            x=el.count*float(el.product.price)*1000
            msg += f"{el.count}✖️{el.product.name}  {x} sum \n"
            summm+=x

        try:
            delevery_place = Location.objects.get(distanations=context.user_data['manzil'])
            msg+=f"\nYitkazib berish: {delevery_place.shipment_cost} sum\n"
            summm+=delevery_place.shipment_cost
        except Exception as err:
            print("xato:"+err)
            # pass

        msg+=f"     <b>Jami: {summm}</b>"
        
            

        context.bot.send_message(chat_id=-1001973681939, text=msg,parse_mode="HTML")
        context.bot.send_message(chat_id=query.message.chat_id,
                                 text="✅Buyurtma qabul qilindi !\nBosh menyu:",reply_markup=menu_keyboard.home_keyboard())
        
        context.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
        return CHOOSE

    
    
    return CATEGORY_LIST   


    # user_name = update.message.from_user.username
    # the_user = BotUser.objects.get(username=user_name)
    # obj=Basket.objects.filter(user=the_user)[0]
    # mahsulot=int(obj.count*float(obj.price)*1000)
    # msg+=f"<b>{obj.count}ta {obj.product}:</b> {mahsulot} sum\n"
    # try:
    #     shipment_fee=str(context.user_data['shipment']) 
    #     msg=msg+ "<b>Yitkazib berish: <b/>" + shipment_fee + " sum"
    #     msg=msg+f"<b>\nJami:</b> {float(shipment_fee) + mahsulot}\n\n"
    # except Exception as err:
    #     # print(err)
    #     pass
        #     photo_urls.append(el.product.photo)
    #     captions.append(el.product.description)

    # media_group = [
    #     InputMediaPhoto(media=photo_url, caption=caption)
    #     for photo_url, caption in zip(photo_urls, captions)
    # ]  


    # bot.send_media_group(chat_id=update.message.from_user.id,text=letter+"testtt\n" ,media=media_group)
        







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
    u = BotUser.objects.get(user_id=user.id)
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
    if update.message.text == static_text.back:
        update.message.reply_text(f"Bosh sahifa ", reply_markup=menu_keyboard.home_keyboard())
    else:
        number = BotUser.objects.get(user_id=user.id)   
        number = number.contact_number

        for admin_id in ADMINS:
            context.bot.send_message(chat_id=admin_id, text=
            f"USER:  {user.full_name}\n" \
            f"username: @{user.username}\n" \
            f"Cell phone: {number}" \
            f"\n\n💬xabar yubordi👇🏻:\n" \
            f"{update.message.text}"
            )
     
        update.message.reply_text(text=f"{user.first_name} Fikr-mulohazangiz uchun rahmat ",
                                  reply_markup=menu_keyboard.home_keyboard())
        
    return CHOOSE


    # LANGUAGES SETTINGS....
def settings(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Harakat tanlang:", reply_markup=menu_keyboard.entry_lg())
    
    return GET_LANGUAGE

def get_lg(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    
    if update.message.text == static_text.back:
        update.message.reply_text(f"Bosh sahifa ", reply_markup=menu_keyboard.home_keyboard())
    else:
        update.message.reply_text("Tilni tanlang:", reply_markup=menu_keyboard.choose_lg())
        

    return HAVE_DONE

def have_done(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(f"✅ Tayyor !", reply_markup=menu_keyboard.home_keyboard())
        
    return CHOOSE


