import datetime

def calc_time_s(inicio,proxy_new,chat,sms,bot):
    fin = datetime.datetime.now()
    final = datetime.datetime(fin.year, fin.month, fin.day, fin.hour,fin.minute,fin.second)
    result = final-inicio
    msg = f'🥳 <b>Congratulations !!!</b>\nProxy Encontrado 🔎\n<b>🕰 TT : </b>{result}\n<pre>socks5://{proxy_new}</pre>'
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode="HTML",text=msg)

def calc_time_e(inicio,chat,sms,bot,texto):
    fin = datetime.datetime.now()
    final = datetime.datetime(fin.year, fin.month, fin.day, fin.hour,fin.minute,fin.second)
    result = final-inicio
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode="HTML",text=texto+f'\n\n<b>🕰 TT : </b>{result}')

def calc_time_l(inicio,proxy_new,chat,sms,bot):
    fin = datetime.datetime.now()
    final = datetime.datetime(fin.year, fin.month, fin.day, fin.hour,fin.minute,fin.second)
    result = final-inicio
    msg = f'Proxy Encontrado 🔎 : \n<pre>socks5://{proxy_new}</pre> \n<b>🕰 TT : </b>{result}'
    bot.sendMessage(chat_id=chat,parse_mode="HTML",text=msg)

def calc_time(inicio):
    fin = datetime.datetime.now()
    final = datetime.datetime(fin.year, fin.month, fin.day, fin.hour,fin.minute,fin.second)
    result = final-inicio
    print('Tiempo Transcurrido : '+str(result))