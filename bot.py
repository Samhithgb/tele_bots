#188677838:AAF7kSyEiYCXIEZLBPfU6QNQwcqF8gWGrFw

import sys
import time
import pprint
import telepot
import requests
import json

def handle(msg):
    global bot
    pprint.pprint(msg)
    l=msg['chat']
    k=l['id']
    bot.sendMessage(k,"Hello Human!")   
    #pprint.pprint(msg['chat'])
    # Do your stuff here ...


# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.
TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
