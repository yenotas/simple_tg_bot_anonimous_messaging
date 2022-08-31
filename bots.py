# -*- coding: utf-8 -*-
from requests import post, get as rget
from os import path

def getname(u):
    e = {}
    e[0] = str(u['chat']['id'])
    e[1] = e[0]
    if 'username' in u['chat']:
        e[0] = u['chat']['username']
    if 'first_name' in u['chat']:
        e[1] = u['chat']['first_name']
        if 'last_name' in u['chat']:
            e[1] += ' ' + u['chat']['last_name']
    return e

def mass_forward_mess(bot_id, txt):
    print('массовая рассылка', txt)
    return

def send_mess(botid, tid, text, reply_to_message_id=None):
    method = 'sendMessage'
    url = f'https://api.telegram.org/bot{botid}/{method}'
    data = {'chat_id': tid, 'text': text, 'parse_mode': 'HTML'}
    if reply_to_message_id:
        data['reply_to_message_id'] = reply_to_message_id
    req = post(url, data=data)
    print(req)
    if req.status_code == 200:
        return True
    else:
        return False
    
def pin_mess(botid, tid, id):
    method = 'pinChatMessage'
    url = f'https://api.telegram.org/bot{botid}/{method}'
    data = {'chat_id': tid, 'message_id': id}
    req = post(url, data=data)
    return True

def get_file(botid, sticker_id):
    method = 'getFile'
    url = f'https://api.telegram.org/bot{botid}/{method}?file_id={sticker_id}'
    print(url)
    resp = rget(url)
    return resp.json()['result']['file_path']

def forward_mess(botid, tid, fromid, mesid):
    method = 'forwardMessage'
    url = f'https://api.telegram.org/bot{botid}/{method}'
    data = {'chat_id': tid, 'from_chat_id': fromid, 'message_id': mesid}
    req = post(url, data=data)
    return True

def del_mess(botid, tid, id):
    method = 'deleteMessage'
    url = f'https://api.telegram.org/bot{botid}/{method}'
    data = {'chat_id': tid, 'message_id': id}
    req = post(url, data=data)
    return True

def send_doc(botid, tid, id, caption):
    method = 'sendDocument'
    url = f'https://api.telegram.org/bot{botid}/{method}'
    data = {'chat_id': tid, 'caption': caption, 'document': id, 'parse_mode': 'HTML'}
    req = post(url, data=data)
    return True

def send_photo(botid, tid, id, caption):
    method = 'sendPhoto'
    url = f'https://api.telegram.org/bot{botid}/{method}'
    data = {'chat_id': tid, 'caption': caption, 'photo': id, 'parse_mode': 'HTML'}
    req = post(url, data=data)
    print(req)
    return True

def send_mem_photo(botid, uid, fn):
    method = 'sendDocument'
    url = f'https://api.telegram.org/bot{botid}/{method}'
    f = open(fn, 'r', encoding='utf-8', errors='ignore')
    post_data = {'chat_id': uid, 'caption': fn.split('/')[-1]}
    post_file = {'document': f}
    req = post(url, data=post_data, files=post_file)
    print(f'\nsend_file: стикер отправлен', fn, req)
    f.close

    print(req)
    return True

def checkBlackList(uid):
    BlackList = []
    if uid in BlackList:
        return True
    return False