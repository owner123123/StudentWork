import telebot
from datetime import datetime, timedelta

import telebot.types
import telebot.types
import telebot.types


TOKEN="8273980711:AAHSmRcfxTC60IWI_bn5IdAhuEQVfyN31eA" # токен бота

bot=telebot.TeleBot(TOKEN) # создаем бота

zapis={} # хранилище записей
temp_data={} # временные данные пользователя

def get_time_slots(): # генерация временных слотов на завтра
    slots=[] #создаем пустой список для слотов
    tomorrow=datetime.now()+timedelta(days=1) # получаем дату завтрашнего дня
    for hour in range(9,18): # цикл от 9 до 17 часов
        time_str=tomorrow.strftime(f"%d.%m.%y {hour}:00") # форматируем дату и время в строку
        slots.append(time_str) # добавляем слот в список
    return slots # возвращаем список всех слотов
@bot.message_handler(commands=['start']) # обработчик комманды start
def start(message): # отправляем сообщение которое ниже
    bot.send_message(message.chat.id,"Привет! я бот для записи!\n\n Комманды:\n/book - записаться \n /myrecord- моя запись \n /cancel-отмена\n")
@bot.message_handler(commands=['book']) #обработчик комманды book
def book(message):# отправляем сообщение которое ниже
    chat_id=message.chat.id # отправляем сообщения с просьбой ввести имя
    msg=bot.send_message(chat_id,"Введите ваше имя") # отправляем сообщения с просьбой ввести имя
    bot.register_next_step_handler(msg,get_name) # регестрируем следующий шаг

def get_name(message): # получение имени
    chat_id=message.chat.id # получаем айди чата
    name=message.text # получаем текст сообщения (имя)
    temp_data[chat_id]={'name':name} # сохраняем имя во временной словарь
    slots=get_time_slots() # получаем список всех слотов
    free_slots=[] # создаем список свободных слотов
    for slot in slots: # перебираем все слоты 
        if slot not in zapis: # если слота нет в записях
            free_slots.append(slot) # добавляем в список свободных
        if not free_slots: # добавляем в списрок свободных
            bot.send_message(chat_id,"Извините, на завтра нет свободного времени") # если список пуст то сообщаем что свободного времени пока что нету
            return # завершение функции
    markup=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True) # создаем клавиатуру с кнопками
    buttons=[] # список для кнопок
    for slot in free_slots[:8]: #  берем первые 8 свободных слотов
            buttons.append(telebot.types.KeyboardButton(slot)) # создаем кнопку для каждого свободного слота
            markup.add(*buttons) # создаем папку для каждого слота
            msg=bot.send_message(chat_id,"Приятно познакомиться, {Name} !\n Выберите свободное время", reply_markup=markup) # отправляем слообщения с клавиатурой для выбора времени
            bot.register_next_step_handler(msg,get_time) # регистрируем следующий шаг
def get_time(message): # функция для получения своодного времеин
    chat_id=message.chat.id # получаем id чата
    selected_time=message.text # получаем выбранное время
    if selected_time in zapis: # сообщаем что уже занято
        bot.send_message(chat_id, "Это время уже занято! Начните заново /book", reply_markup=telebot.types.ReplyKeyboardRemove) #
        return # завершение функции
    name=temp_data[chat_id]['name'] # получаем время из временного хранилища
    zapis[selected_time]=name # сохраняем запись
    bot.send_message(chat_id, # отправляем подтверждение записи и убираем клавиатуру
                        f"Имя{name}\n" # 
                        f"Время: {selected_time} \n\n" # 
                        f"Ждем вас!", reply_markup=telebot.types.ReplyKeyboardRemove()) # 
    del temp_data[chat_id] # удаляем временные данные пользователя
def my_record(message): # обработчик комманлы myrecord
    chat_id=message.chat.id # 
    user_name=message.from_user.first_name # 
    found=False # 
    for time,name in zapis.items(): # 
        if name == user_name: # если имя совпадает с именем в записи
            bot.send_message(chat_id,f"Ваша запись: {time}") # отпарялем информацию о записи
            found=True # устанавливаем флаг
            break # прерываем цикл
        if not found: # 
            bot.send_message(chat_id,"У вас нет активных записей") # 
bot.polling(non_stop=True)