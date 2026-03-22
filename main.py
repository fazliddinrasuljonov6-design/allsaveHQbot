import telebot
import yt_dlp
import os

# Tokenni Render Environment Variable'dan oladi
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! @AllSaveHQbot tayyor. 📥\nVideo linkini yuboring!")

@bot.message_handler(func=lambda m: True)
def download(message):
    url = message.text
    if "http" in url:
        msg = bot.reply_to(message, "Yuklanmoqda... ⏳")
        file_name = f"{message.chat.id}.mp4"
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': file_name,
            'noplaylist': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            with open(file_name, 'rb') as video:
                bot.send_video(message.chat.id, video, caption="✅ Yuklab olindi!\n@AllSaveHQbot")
            
            os.remove(file_name)
            bot.delete_message(message.chat.id, msg.message_id)
        except Exception as e:
            bot.reply_to(message, "Xatolik yuz berdi. Linkni tekshiring.")
            if os.path.exists(file_name):
                os.remove(file_name)
    else:
        bot.reply_to(message, "Iltimos, link yuboring.")

bot.polling(none_stop=True)
