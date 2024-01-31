import telebot 
import time
import os 
import requests
from users import *
from dotenv import load_dotenv 
load_dotenv()
from send_discord import send_message_to_discord, send_photo_to_discord, thread_to_thread,send_doc_to_discord, send_mp4_to_discord


telegram_token =  "6857058553:AAFwlBN1zOdi8vKYhWwE8Q_dTQc2_iacL7o"
bot = telebot.TeleBot(telegram_token, parse_mode='Markdown')


def get_message_link(chat_id, message_id):
    return f"https://t.me/{bot.get_me().username}?chat_id={chat_id}&message_id={message_id}"


@bot.message_handler(content_types=['photo','text','document','animation','video'], func=lambda message: message.chat.id == ???)
def message_spotter(message):  

    telegram_thread = message.message_thread_id
    name = message.from_user.first_name
    pfp = pfp_retriever(name)

    # try:
    #   webhook = webhook.format(thread = thread_to_thread[telegram_thread])
    # except: 
    #   print (f"Thread {telegram_thread} not added yet")


    if message.photo:
      print ("Hey!")
      text = message.caption
      file_id = message.photo[-1].file_id
      file_info = bot.get_file(file_id)
      file = requests.get(f'https://api.telegram.org/file/bot{telegram_token}/{file_info.file_path}')
      with open('photo.png','wb') as f:
        f.write(file.content)
        print ("Image saved")
      send_photo_to_discord(text, name, pfp)
      time.sleep(1)

    elif message.document or message.video:
      text = message.caption 
      if message.document:
        file_id = message.document.file_id 
        file_size = message.document.file_size
      else: 
        file_id = message.video.file_id
        file_size = message.video.file_size

      if int(file_size) < 8*1024*1024: #8mb
        print ("Smaller than 8MB")
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        if message.document:
          save_path = '/home/tony/Desktop/comms/' + message.document.file_name
        else:         
          save_path = '/home/tony/Desktop/comms/' + message.video.file_name

        with open(save_path, 'wb') as new_file:
          new_file.write(downloaded_file)
        if message.document: 
          send_doc_to_discord(text,name,pfp,save_path)
        else: 
          send_mp4_to_discord(text,name,pfp,save_path)
      
      else: 
        message_link = get_message_link(message.chat.id, message.message_id)
        print (message_link)

    elif message.video: 
      print ("this is a video")

    else: 
      text = message.text
      send_message_to_discord(text, name, pfp)
      time.sleep(1)

    
  

bot.infinity_polling()


    # try: 
    #   if message.photo: 
    #     text = message.caption
    #     if replying_to != None:
    #       if message.caption != None:
    #         text = f"-----------\nReply to {repliying_to_user}\n💬 ``{replying_to}``\n    \n{text}\n----------- "
    #       else:       
    #         text = f"-----------\nReply to {repliying_to_user}\n💬 ``{replying_to}``\n    \n----------- "


    #   else: 
    #     text = message.text
    #     if replying_to: 
    #        text = f"-----------\nReply to {repliying_to_user}\n💬 ``{replying_to}``\n    \n{text}\n----------- "
    #     send_message_to_discord(text, name, pfp, webhook)
    #     time.sleep(1)
    # except: 
    #     print (f"User not in Comms Department: {name}")