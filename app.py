# -*- coding: utf-8 -*-

import sys
from os import path

sys.path.insert(0, path.dirname(__file__))

import json
from flask import Flask, request, jsonify
from requests import post

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    return 'bot is running'

from config import BOT, bot_addr, sitelink, ADMINS, yreq, please, tglang, repl, case
from bots import send_mess, del_mess

lang = 'en'

def sethook():
    r = post(f'https://api.telegram.org/bot{BOT}/setWebhook?url={sitelink + bot_addr}')
    return

# sethook()

def transl(s):

    re = ''
    try:
        re = repl[s[3]][s[0]]
        for i in range(4, len(s)):
            if s[i]:
                re += repl[s[3]][case.get(i, None)] + s[i]
        re += '.' + repl[s[3]][case.get(1, None)] + s[1] + repl[s[3]][case.get(2, None)] + s[2]
        if len(s) > 1: 
            lang = s[3]
    except:
        pass
    return re


@app.route(bot_addr, methods = ['POST']) 
def in_hub():
    global tglang

    update = ''
    json_string = ''
    try:
        json_string = request.get_data().decode('utf-8')
        update = json.loads(json_string)
    except:
        update = ''
        
    if update:
        if "language_code" in str(update):
            tglang = str(update).split("language_code': '")[1][0:2]

        message = update['message']
        mes = ''
        uid = message['chat']['id']

        uname = ''
        fullname = ''
        txt = ''

        if 'username' in message['chat']:
            uname = message['chat']['username']
        if 'first_name' in message['chat']:
            fullname = message['chat']['first_name']
        if 'last_name' in message['chat']:
            fullname += " " + message['chat']['last_name']


        if 'bot_command' in str(message):
            txt = message['text'].split(' ')[1].split('_')
            mid = int(message['message_id'])
            if len(txt) < 3: return {'ok': 200}
            t = transl(txt)
            # print(t)
            if t:
                send_mess(BOT, ADMINS[0], f"<b>От: @{uname}|{fullname}</b>|{message['chat']['id']}|{message['message_id']}|{tglang}|"+chr(10)+f"<i>{t}</i>")
            
            send_mess(BOT, uid, yreq[lang]+chr(10)+t+chr(10)+chr(10)+please[lang])
            del_mess(BOT,uid, mid)
            return {'ok': 200}


        req = ''
        if 'private' in str(message) and not uid in ADMINS:
            mes = message['text']
            send_mess(BOT, ADMINS[0], f"<b>От: @{uname}|{fullname}</b>|{message['chat']['id']}|{message['message_id']}|{tglang}|"+chr(10)+f"<i>{mes}</i>")
            return {'ok': 200}

        elif uid in ADMINS:

            admin = message['chat']['id']
            data = str(message).split('|')
            if len(data) == 6:
                try:
                    if not send_mess(BOT, data[2], "<b>Terasa Bartula:</b>"+chr(10)+message['text'], reply_to_message_id=int(data[3])):
                        req = send_mess(BOT, data[2], "<b>Terasa Bartula:</b>"+chr(10)+message['text'])
                        if not req:
                            send_mess(BOT, ADMINS[0], 'Это сообщение не доставлено:   '+message['text'])

                except Exception as e:
                    pass

            else:
                del_mess(BOT, admin, message['message_id'])
            return {'ok': 200}
                        

    return {'ok': 200}