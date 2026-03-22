import telebot
import yt_dlp
import os

TOKEN = '8403066362:AAFJSYJLWVa_OpRbcUlK7v2J4U6LveTGlN4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Link yuboring, videoni yuklab beraman. ✅")

@bot.message_handler(func=lambda m: True)
def download(message):
    url = message.text
    if "http" in url:
        msg = bot.reply_to(message, "Yuklanmoqda...")
        ydl_opts = {'format': 'best', 'outtmpl': 'v.mp4', 'noplaylist': True}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            with open('v.mp4', 'rb') as video:
                bot.send_video(message.chat.id, video, caption="@AllSaveHQbot")
            os.remove('v.mp4')
            bot.delete_message(message.chat.id, msg.message_id)
        except Exception as e:
            bot.reply_to(message, "Xatolik!")
    else:
        bot.reply_to(message, "Link yuboring.")

bot.polling()
