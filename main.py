import os
import telebot
import yt_dlp
from flask import Flask # Buni qo'shdik

# Render uchun kichik veb-server (Port xatosini yo'qotish uchun)
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

# Bot qismi
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men tayyorman. Link yuboring!")

@bot.message_handler(func=lambda m: True)
def download(message):
    url = message.text
    if "http" in url:
        # Avvalgi yuklash kodingiz shu yerda qoladi...
        bot.reply_to(message, "Yuklash boshlandi...")
        # ... (yuklash kodi)

# Botni va Veb-serverni parallel ishga tushirish
if __name__ == "__main__":
    # Botni alohida "threading" bilan ishga tushirish qiyin bo'lsa, 
    # shunchaki pollingni ishga tushiramiz
    import threading
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))).start()
    
    print("Bot ishga tushdi...")
    bot.polling(none_stop=True)
