from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import time

def log(update: Update, _):
    file = open('db.csv', 'a', encoding = 'utf-8')
    file.write(f'{time.ctime(time.time())}|{update.effective_user.first_name}|{update.effective_user.id}|{update.message.text}\n')
    file.close