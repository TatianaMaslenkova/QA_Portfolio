from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler
from telegram import Update
from anecAPI import anecAPI
from config import TOKEN

def get_joke(update: Update, context: CallbackContext):
    after_command = context.args
    print(after_command)
    update.message.reply_text(anecAPI.modern_joke())


def get_message(update: Update, context: CallbackContext):
    message = update.message.text
    print(message)
    if 'прив' in message: 
        update.message.reply_text(f'Взаимно Приветствую!') 
        return None 
    update.message.reply_text(f'вы ввели: {message}')    


updater = Updater(TOKEN)
dispetcher = updater.dispatcher

joke_handler = CommandHandler('joke', get_joke)
message_handler = MessageHandler(Filters.text, get_message)

dispetcher.add_handler(joke_handler)
dispetcher.add_handler(message_handler)



print('сервер запущен')
updater.start_polling()
updater.idle()
