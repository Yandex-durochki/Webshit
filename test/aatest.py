import sqlite3
import os
import requests
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext):
    # Получаем параметр username из ссылки
    username = context.args[0]
    
    # Получаем файл с информацией о пользователе
    profile_photo = context.bot.get_user_profile_photos(update.message.from_user.id).photos[0][-1].get_file()
    photo_url = profile_photo.file_path
    
    # Скачиваем фото профиля
    photo_path = f"photos/{username}_photo.jpg"
    photo_file = requests.get(photo_url).content
    with open(photo_path, 'wb') as file:
        file.write(photo_file)
    
    # Сохраняем путь к фото в базу данных
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (username, sourceimg) VALUES (?, ?)", (username, photo_path))
    conn.commit()
    conn.close()
    
    # Отправляем сообщение пользователю
    update.message.reply_text("Успешная регистрация")

# Создаем базу данных SQLite для хранения информации о пользователях
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                (id INTEGER PRIMARY KEY, username TEXT, sourceimg TEXT)''')
conn.commit()
conn.close()

# Запускаем бота
updater = Updater('6804116038:AAGJtBz8CerZ2SqjMQuunyXZ4z0mp7IvXOI', use_context=True)
dispatcher = updater.dispatcher

# Добавляем обработчик команды /start
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
