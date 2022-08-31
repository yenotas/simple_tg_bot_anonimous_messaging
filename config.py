# -*- coding: utf-8 -*-
BOT = "5123029165:AAHyiY-wWuFQJbDqKg19lm44CZiDXrYTYM4"
bot_addr = "/tb"
sitelink = "https://bot.terasabartula.com"
ADMINS = [1056908825]
yreq = {
    'ru': 'Ваш запрос:',
    'en': 'Your request:',
    'cg': 'Vaš upit:'
    }
please = {
        'ru': 'Если что-то не верно - напишите, администратор скоро ответит!',
        'en': 'If something is wrong - write, the administrator will answer soon!',
        'cg': 'Ako nešto nije u redu - napišite, administrator će uskoro odgovoriti!'
        }
tglang = ''

case = {1: 'id', 2: 'tel', 3: 'lang', 4: 'dEvent', 5: 'startT', 6: 'endT', 7: 'evType', 8: 'gCount' }
repl = {
    'ru': {'R': 'Хочу зарезирвировать мероприятие на ', 'id': ' id: ', 'C': 'Я хочу изменить ', 'dEvent': 'дату ', 'tel': ', тел: ', 'startT': ' с ', 'endT': ' до ', 'evType': '. Вид события: ', 'gCount': ', гостей: '},
    'en': {'R': 'I want to reserve an event for a ', 'id': ' id: ', 'C': 'I want to change the ', 'dEvent': 'date of ', 'tel': ', tel: ', 'startT': ' from ', 'endT': ' to ', 'evType': '. Event type: ', 'gCount' : ', guests: '},
    'cg': {'R': 'Želim rezervirati događaj za ', 'id': ' id: ', 'C': 'Želim promijeniti ', 'dEvent': 'datum ', 'tel': ', tel: ', 'startT': ' od ', 'endT': ' do ', 'evType': '. Vrsta događaja: ', 'gCount' : ', gosti: ' }
    }