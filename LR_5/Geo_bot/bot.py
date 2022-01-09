import telebot

token = '5003951699:AAEKuKclpMbKuvrLYXL90Ju1m4N_ByJETzo'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
 keyboard = telebot.types.ReplyKeyboardMarkup(True)
 keyboard.row('Испания', 'Франция', 'Италия', 'Португалия')
 bot.send_message(message.chat.id, 'Урок географии. Столицу какой страны тебе показать?',
reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
 if message.text.lower() == 'испания':
   bot.send_message(message.chat.id, 'Мадрид')
   p = open ("Madrid.jpg", 'rb')
   bot.send_photo(message.chat.id, p)
 elif message.text.lower() == 'франция':
   bot.send_message(message.chat.id, 'Париж')
   c = open("Paris.jpg", 'rb')
   bot.send_photo(message.chat.id, c)
 elif message.text.lower() == 'италия':
   bot.send_message(message.chat.id, 'Рим')
   b = open("Rome.jpg", 'rb')
   bot.send_photo(message.chat.id, b)
 elif message.text.lower() == 'португалия':
   bot.send_message(message.chat.id, 'Лиссабон')
   t = open("Lissabon.jpg", 'rb')
   bot.send_photo(message.chat.id, t)

bot.polling()