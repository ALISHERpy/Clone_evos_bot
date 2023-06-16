from telegram.ext import (
    Dispatcher, Filters,
    CommandHandler, MessageHandler,
    CallbackQueryHandler,
)

from dtb.settings import DEBUG
from tgbot.handlers.broadcast_message.manage_data import CONFIRM_DECLINE_BROADCAST
from tgbot.handlers.broadcast_message.static_text import broadcast_command
from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.menu import handlers as menu_handlers
from tgbot.handlers.menu import static_text as menu_text 
from tgbot.handlers.location import static_text as location_text

from tgbot.handlers.utils import files, error
from tgbot.handlers.admin import handlers as admin_handlers
from tgbot.handlers.location import handlers as location_handlers
from tgbot.handlers.onboarding import handlers as onboarding_handlers
from tgbot.handlers.broadcast_message import handlers as broadcast_handlers
from tgbot.main import bot
from tgbot.states import *
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)



def setup_dispatcher(dp):
    dp.add_handler(CommandHandler("admin", admin_handlers.admin))
    dp.add_handler(CommandHandler("stats", admin_handlers.stats))
    dp.add_handler(CommandHandler('export_users', admin_handlers.export_users))
    
    

    #  = map(chr, range(8))
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", menu_handlers.home_page)],
        states={
            HOME: [MessageHandler(Filters.text, menu_handlers.home_page)],
            CHOOSE: [
                MessageHandler(Filters.regex(f"^{menu_text.home_menu}$"),  menu_handlers.click_menu),
                MessageHandler(Filters.regex(f"^{menu_text.home_my_orders}$"),  menu_handlers.my_orders),
                MessageHandler(Filters.regex(f"^{menu_text.home_comment}$"),  menu_handlers.comment),
                MessageHandler(Filters.regex(f"^{menu_text.home_settings}$"),  menu_handlers.settings),
                
                
            ],
            MENU: [
                MessageHandler(Filters.regex(f"^{menu_text.address_my_addresses}$"),  menu_handlers.address_list),
                MessageHandler(Filters.location, location_handlers.location_handler),
                # Filters.regex(f"^{menu_text.address_send_location}$"),  menu_handlers.send_location,
                MessageHandler(Filters.regex(f"^{menu_text.back}$"),  menu_handlers.home_page),
            ],
            ADDRESSES_LIST: [
                MessageHandler(Filters.regex(f"^{menu_text.back}$"), menu_handlers.click_menu),
                MessageHandler(Filters.text, menu_handlers.category_list),
                
            ],
            
            WRITE_COMMENT: [MessageHandler(Filters.contact, menu_handlers.write_comment)],
            COMMENT_DONE: [MessageHandler(Filters.text, menu_handlers.comment_done)],

            GET_LANGUAGE: [MessageHandler(Filters.text, menu_handlers.get_lg)],
            HAVE_DONE: [MessageHandler(Filters.text, menu_handlers.have_done)],

            LOCATION_CONFIRM:  [
                MessageHandler(Filters.regex(f"^{location_text.yes}$"),  menu_handlers.category_list),
                # Filters.regex(f"^{menu_text.address_send_location}$"),  menu_handlers.send_location,
                MessageHandler(Filters.regex(f"^{location_text.no}$"),  menu_handlers.click_menu),
            ],

            # MY_ORDERS: [MessageHandler(Filters.regex(f"^{menu_text.home_my_orders}"), )],
            # COMMENT: [],
            # SETTINGS: [],
            # MY_ADDRESSES: [MessageHandler(Filters.regex(f"^{menu_text.address_my_addresses}$"), menu_handlers.address_list)],
            # SEND_LOCATION: [MessageHandler(Filters.regex(f"^{menu_text.address_send_location}$"), menu_handlers.)],
            
        },
        fallbacks=[MessageHandler(Filters.text & ~Filters.command, menu_handlers.home_page)],
    )

    dp.add_handler(conv_handler)

    # location
    dp.add_handler(CommandHandler("ask_location", location_handlers.ask_for_location))
    #location kelsaa
    # CONVERSATION HANDLER ICHIDA BO'lishi kerak bu  okkk


    # secret level
    dp.add_handler(CallbackQueryHandler(onboarding_handlers.secret_level, pattern=f"^{SECRET_LEVEL_BUTTON}"))

    # broadcast message
    dp.add_handler(
        MessageHandler(Filters.regex(rf'^{broadcast_command}(/s)?.*'), broadcast_handlers.broadcast_command_with_message)
    )
    dp.add_handler(
        CallbackQueryHandler(broadcast_handlers.broadcast_decision_handler, pattern=f"^{CONFIRM_DECLINE_BROADCAST}")
    )

    # files
    dp.add_handler(MessageHandler(
        Filters.animation, files.show_file_id,
    ))

    #NONE_OF_THEM
    

    # handling errors
    dp.add_error_handler(error.send_stacktrace_to_tg_chat)

    # EXAMPLES FOR HANDLERS
    # dp.add_handler(MessageHandler(Filters.text, <function_handler>))
    # dp.add_handler(MessageHandler(
    #     Filters.document, <function_handler>,
    # ))
    # dp.add_handler(CallbackQueryHandler(<function_handler>, pattern="^r\d+_\d+"))
    # dp.add_handler(MessageHandler(
    #     Filters.chat(chat_id=int(TELEGRAM_FILESTORAGE_ID)),
    #     # & Filters.forwarded & (Filters.photo | Filters.video | Filters.animation),
    #     <function_handler>,
    # ))

    return dp


n_workers = 0 if DEBUG else 4
dispatcher = setup_dispatcher(Dispatcher(bot, update_queue=None, workers=n_workers, use_context=True))

