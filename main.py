import os
import telebot
from PIL import Image
from loguru import logger
from translate import Translator
from pytesseract import pytesseract


token = os.getenv('TELEGRAM_KEY') 
bot = telebot.TeleBot(token)

try:
    @bot.message_handler(commands=['start', 'info'])
    def start(message):
        start_message = "Hello and Welcome, my name is Transalte bot. Send me a message and i try to find anu text"
        bot.send_message(message.chat.id, start_message, parse_mode='html') #Start Commands

    @bot.message_handler(content_types=['photo'])
    def photo(message):   
        fileID = message.photo[-1].file_id   
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
            # Get photo from user

        row = Image.open("image.jpg")
        data = pytesseract.image_to_string(row) # Open and read

        if (not(data and data.strip())):  # Check about has string some data
            logger.debug("SomeOne send empty photo")
            bot.send_message(message.chat.id, "The Program Cant find any text on this image Sorry!")

        else:
            bot.send_message(message.chat.id, 'processing...', parse_mode='html')
            bot.send_message(message.chat.id, data, parse_mode='html')
            bot.send_message(message.chat.id, 'Do you want translate it to Russian? yes no')

# Send results


            @bot.message_handler()
            def get_user_text(message):
                if message.text == 'no' or message.text == 'No':
                    bot.send_message(message.chat.id, "OKKKKKK", parse_mode='html')

                elif message.text == 'yes' or message.text == 'Yes':

                    translator = Translator(from_lang="en", to_lang="ru")
                    rowdata = f"""{data}"""
                    translation = translator.translate(rowdata)
                    bot.send_message(message.chat.id, translation, parse_mode='html')

                else:
                    bot.send_message(message.chat.id, "Sorry , i can't understand you!")


    bot.polling(none_stop=True)

except KeyboardInterrupt:
    logger.error("KeyboardInterrupt. The Program Stopped!")
