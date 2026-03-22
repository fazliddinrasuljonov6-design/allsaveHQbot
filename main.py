import telebot
import yt_dlp
import os

# DIQQAT: Tokeningizni quyidagi qo'shtirnoq ichiga yozing
TOKEN = '8403066362:AAFJSYJLWVa_OpRbcUlK7v2J4U6LveTGlN4' 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! @AllSaveHQbot tayyor. 📥\nVideo linkini yuboring (Instagram, YouTube, TikTok)!")

@bot.message_handler(func=lambda m: True)
def download_video(message):
    url = message.text
    if "http" in url:
        msg = bot.reply_to(message, "Yuklanmoqda... ⏳ (Sifat tekshirilmoqda)")
        
        # Fayl nomi foydalanuvchi IDsi bilan (bir vaqtda bir necha kishi ishlatsa xato bermasligi uchun)
        file_name = f"video_{message.chat.id}.mp4"
        
        ydl_opts = {
            'format': 'best', # Eng yaxshi sifatni tanlaydi
            'outtmpl': file_name,
            'noplaylist': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # Videoni yuborish
            with open(file_name, 'rb') as video:
                bot.send_video(message.chat.id, video, caption="✅ @AllSaveHQbot orqali yuklab olindi!")
            
            # Server xotirasini tozalash (faylni o'chirish)
            os.remove(file_name)
            bot.delete_message(message.chat.id, msg.message_id)
            
        except Exception as e:
            bot.reply_to(message, f"Xatolik yuz berdi: Link noto'g'ri yoki video juda katta.")
            if os.path.exists(file_name):
                os.remove(file_name)
    else:
        bot.reply_to(message, "Iltimos, haqiqiy video linkini yuboring.")

print("Bot ishga tushdi...")
bot.polling(none_stop=True)
