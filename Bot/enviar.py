#!/usr/bin/python
import sys
import time
import telepot
#import cookie
from telepot.loop import MessageLoop
import pdb

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text' and msg["text"].lower() == "PC1_Safe_Gym":
        # let the human know that the pdf is on its way        
        bot.sendMessage(chat_id, "preparing pdf of fresh news, pls wait..")
        file="/home/SafeGym/Pontos_de_controle/PC1_Safe_Gym.pdf"

        # send the pdf doc
        bot.sendDocument(chat_id=chat_id, document=open(file, 'rb'))
    elif content_type == 'text':
        bot.sendMessage(chat_id, "sorry, I can only deliver news")

# replace XXXX.. with your token
TOKEN = '1752787298:AAHuFGnIH4gar_cMpTc-sJjwwwCe22mEO5A'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
# Keep the program running.
while 1:
    time.sleep(10)
