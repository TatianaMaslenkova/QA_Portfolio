from telegram import Update
from telegram.ext import CallbackContext
from logging import *

def hello_function(update: Update, context):
    message = update.message.text
    log(update, context)
    print(message)
    if 'прив' or 'здрав' in message: 
        update.message.reply_text(f'Привет, {update.effective_user.first_name}!') 
        return None
    update.message.reply_text(f'вы ввели: {message}\n Не понял команду, повторите ввод\n')

def start_function(update: Update, context: CallbackContext):
    log(update, context)
    message = update.message.text
    print(message)
    update.message.reply_text(f'Меня зовут Мастер комплексных чисел (общий вид комплексного числа: z = a + bi)\n'
        'Вам нужно выбрать операцию и ввести через пробел 4 числа (если число вещественное, то целая часть отделяется от дробной ".")\n'
        'Доступные действия:\n/hello\n/help - помощь\n/sum - складываю\n/sub - вычитаю\n/prod - умножаю\n/div - делю')

def sum_function(update: Update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    if ',' in msg: 
        update.message.reply_text(error_message1(msg))
    else:
        items = msg.split() # по умолчанию разбивка по пробелу, на выходе /sum 123 456 789 012
        if len(items) < 5:
            update.message.reply_text(error_message2(msg))    
        elif not items[1].isalpha() and not items[2].isalpha() and not items[3].isalpha() and not items[4].isalpha():
            a = float(items[1])
            b = float(items[2])
            c = float(items[3])
            d = float(items[4])

    update.message.reply_text(f'z1 = {a} + {b}i, z2 = {c} + {d}i, z1 + z2 = {(a+c)} + {(b+d)}i')

def sub_function(update: Update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    if ',' in msg: 
        update.message.reply_text(error_message1(msg))
    else:
        items = msg.split()
        if len(items) < 5:
            update.message.reply_text(error_message2(msg))    
        elif not items[1].isalpha() and not items[2].isalpha() and not items[3].isalpha() and not items[4].isalpha():
            a = float(items[1])
            b = float(items[2])
            c = float(items[3])
            d = float(items[4])

    update.message.reply_text(f'z1 = {a} + {b}i, z2 = {c} + {d}i, z1 - z2 = {(a-c)} + {(b-d)}i')

def mult_function(update: Update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    if ',' in msg: 
        update.message.reply_text(error_message1(msg))
    else:
        items = msg.split()
        if len(items) < 5:
            update.message.reply_text(error_message2(msg))    
        elif not items[1].isalpha() and not items[2].isalpha() and not items[3].isalpha() and not items[4].isalpha():
            a = float(items[1])
            b = float(items[2])
            c = float(items[3])
            d = float(items[4])

    update.message.reply_text(f'z1 = {a} + {b}i, z2 = {c} + {d}i, z1 * z2 = {(a*c - b*d)} + {(b*c + a*d)}i')

def div_function(update: Update, context):
    log(update, context)
    msg = update.message.text
    print(msg)
    if ',' in msg: 
        update.message.reply_text(error_message1(msg))
    else:
        items = msg.split()
        if len(items) < 5:
            update.message.reply_text(error_message2(msg))    
        elif not items[1].isalpha() and not items[2].isalpha() and not items[3].isalpha() and not items[4].isalpha():
            a = float(items[1])
            b = float(items[2])
            c = float(items[3])
            d = float(items[4])

    update.message.reply_text(f'z1 = {a} + {b}i, z2 = {c} + {d}i, z1 * z2 = {(a*c + b*d) / (c**2 + d**2)} + {((b*c - a*d) / (c**2 + d**2))}i')

def error_message1(msg):
    print(f'Ошибка ввода. Целая часть отделяется от дробной "." (точкой). Вы ввели {msg}')

def error_message2(msg):
    print(f'Ошибка ввода. Нужно ввести 4 числа! Вы ввели {msg}')
