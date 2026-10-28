
import os  # Дозволяє отримувати змінні середовища
import telebot  # Імпортуємо бібліотеку Telegram-бота
from telebot import types  # Імпортуємо інструменти для створення кнопок

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Отримуємо токен зі змінної середовища

if not BOT_TOKEN:  # Перевіряємо, чи є токен
    raise ValueError("Токен бота не знайдено!")  # Виводимо помилку, якщо токена немає

bot = telebot.TeleBot(BOT_TOKEN)  # Створюємо об'єкт нашого бота


# ===== КОМАНДА /start =====

@bot.message_handler(commands=["start"])  # Реагуємо на команду /start
def send_welcome(message):  # Створюємо функцію привітання
    bot.reply_to(message, "Привіт! 👋 Я твій Python-бот 🤖")  # Надсилаємо привітання


# ===== КОМАНДА /menu =====

@bot.message_handler(commands=["menu"])  # Реагуємо на команду /menu
def show_menu(message):  # Створюємо функцію меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Створюємо клавіатуру

    button1 = types.KeyboardButton("👋 Привіт")  # Перша кнопка
    button2 = types.KeyboardButton("🐍 Python")  # Друга кнопка

    markup.add(button1, button2)  # Додаємо кнопки до клавіатури

    bot.send_message(message.chat.id, "Обери дію:", reply_markup=markup)  # Показуємо меню

# ===== КОМАНДА /help =====

@bot.message_handler(commands=["help"])  # Реагуємо на команду /help
def send_help(message):  # Створюємо функцію допомоги
    help_text = (  # Формуємо текст із доступними командами
        "🤖 Я Python Study Assistant!\n\n"
        "Мої команди:\n"
        "/start — привітання\n"
        "/menu — показати кнопки\n"
        "/help — отримати допомогу\n\n"
        "Також можеш написати мені будь-яке повідомлення!"
    )
    bot.reply_to(message, help_text)  # Надсилаємо користувачу інструкцію
    
# ===== ОБРОБКА ТЕКСТОВИХ ПОВІДОМЛЕНЬ =====

@bot.message_handler(content_types=["text"])  # Реагуємо на текстові повідомлення
def echo_all(message):  # Створюємо функцію обробки повідомлень

    if message.text == "👋 Привіт":  # Перевіряємо натискання першої кнопки
        bot.reply_to(message, "Вітаю! Рада тебе бачити! 😊")  # Відповідаємо на привітання

    elif message.text == "🐍 Python":  # Перевіряємо натискання другої кнопки
        bot.reply_to(message, "Python — чудова мова програмування! 🐍")  # Відповідаємо про Python

    else:  # Якщо користувач написав інший текст
        bot.reply_to(message, f"Ти написала: {message.text}")  # Повторюємо повідомлення


# ===== ЗАПУСК БОТА =====

print("Бот запущений...")  # Виводимо повідомлення в терміналі
bot.infinity_polling()  # Запускаємо постійне отримання повідомлень
