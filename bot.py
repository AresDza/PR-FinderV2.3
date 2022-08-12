import telegram
from telegram import *
from telegram.ext import *
import S5Crypto
import time
import os
from JDatabase import JsonDatabase
import start
import infoz
import datetime
import time_calc
import PRFinderV3

dev = 1

def iniciado():
    try:bot.sendMessage(chat_id=user_id,text='BOT Reiniciado!!🔋 ')
    except:print("Ejecutando el bot @" + bot.username)

def filtrar_text(update, context):
    text = update.message.text
    chat = update.message.chat.id
    username = update.effective_user.username
    userid = update.effective_user.id
    try :
        jdb = JsonDatabase('database')
        jdb.check_create()
        jdb.load()
        user_info = jdb.get_user(username)
        if username == administrador or user_info :  # Validar Usuario
            if user_info is None:
                if username == administrador:
                    jdb.propietario(username)
                else:
                    jdb.propietario(username)
                user_info = jdb.get_user(username)
                jdb.save()
        else:return
    except:pass

    if '/start' in text:
        getUser = user_info
        if getUser:
            statInfo = start.start_i(username,userid,getUser,jdb.is_admin(username),jdb.listar(username))
            bot.sendMessage(chat_id=chat,parse_mode='HTML',text=statInfo)
            return

    if '/pr_decrypt' in text:
        getUser = user_info
        if getUser:
            proxy_sms = str(text).split(' ')[1]
            sms = bot.sendMessage(chat,'🔎 Procesando Proxy !!🕑..')
            if text.__contains__ ('socks5://'):proxy_sms = str(proxy_sms).split('socks5://')[1]
            else:pass
            proxy_de = S5Crypto.decrypt(f'{proxy_sms}')
            bot.editMessageText(chat_id=chat,message_id=sms.message_id,text='🔎 Procesando Proxy !!🕓...')
            bot.editMessageText(chat_id=chat,message_id=sms.message_id,text='🔎 Procesando Proxy !!🕕..')
            bot.editMessageText(chat_id=chat,message_id=sms.message_id,text='🔎 Procesando Proxy !!🕗...')
            bot.editMessageText(chat_id=chat,message_id=sms.message_id,text='🔎 Procesando Proxy !!🕙..')
            bot.editMessageText(chat_id=chat,message_id=sms.message_id,text='🔎 Procesando Proxy !!🕛...')
            i = 0
            try:
                for i in range(-1,int(len(str(proxy_de).split('.'))-2)) :
                    i+=1
                    nma = int(str(proxy_de).split('.')[i])
                for i in range(-1,1):
                    i+=1
                    nmb = int(str(str(proxy_de).split('.')[int(len(str(proxy_de).split('.'))-1)]).split(':')[i])
            except:
                bot.editMessageText(chat_id=chat,message_id=sms.message_id,text="⚠️ PROXY NO VÁLIDO ❗️")
                print(proxy_de)
                return
            try:
                proxy_ip = str(proxy_de).split(':')[0]
                proxy_port = str(proxy_de).split(':')[1]
                bot.editMessageText(chat_id=chat,message_id=sms.message_id,text=f'🔓Desencriptado Completado:\n\nIP : {proxy_ip}\nPUERTO : {proxy_port}')
            except:
                bot.editMessageText(chat_id=chat,message_id=sms.message_id,text="⚠️ PROXY NO VÁLIDO ❗️")
                print(proxy_de)
            return

    if '/pr_find' in text:
        ini = datetime.datetime.now()
        inicio = datetime.datetime(ini.year, ini.month, ini.day, ini.hour, ini.minute, ini.second)
        getUser = user_info
        if getUser:
            try:
                listar = getUser['listar']
                try:
                    try: #ESPECIFICADO
                        PRFinderV3.prfind_e(bot,chat,time_calc,inicio,username,jdb,user_info,text,botlog,listar,administrador)
                    except: #BUSQUEDA POR IP
                        PRFinderV3.pr_find_thread(text,bot,update,listar)
                except Exception as ex: #POR DEFECTO
                    print(str(ex))
                    if str(ex) != "can't start new thread":PRFinderV3.prfind_p(user_info,bot,chat,username,time_calc,botlog,listar,administrador)
                print('Búsqueda Finalizada!!!')
            except Exception as ex:
                bot.sendMessage(chat,f"✖️ ERROR INESPERADO ✖️\n\n{str(ex)}")
                botlog.sendMessage(chat_id=chat,parse_mode='HTML',text=f"<b>🤖 BOT : </b>@{bot.username}\n<b>🔰 DUEÑO : </b>@{administrador}\n\n<pre>{str(ex)}</pre>")

    if '/listar' in text:
        getUser = user_info
        try:
            if getUser:
                string = str(text).split('_')[1]
                if string == 'on':status = 1
                elif string == 'off':status = 0
                getUser['listar'] = status
                jdb.save_data_user(username,getUser)
                jdb.save()
                listado = '🗒 LISTAR : SI'
                listar = jdb.listar(username)
                if listar:listado = '🗒 LISTAR : NO'
                bot.deleteMessage(chat_id=chat,message_id=update.message.message_id),bot.sendMessage(chat_id=chat,text=listado)
        except:bot.sendMessage(chat_id=chat,text='✖️ ERROR ✖️ Uso Correcto del Comando :\n/listar_on o /listar_off')
        return

    if '/i' in text:
        anim = '.....'
        texto = '⌛️ PROCESANDO '
        bot.deleteMessage(chat_id=chat,message_id=update.message.message_id)
        sms = bot.sendMessage(chat_id=chat,text='⌛️ PROCESANDO ')
        msg=''
        for i in anim:
            msg+=i
            time.sleep(0.10)
            bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode='HTML',text=texto+msg)
        try:
            informacion = str(text).split(' ')[1]
            if informacion.__contains__ ('pr_decrypt'):
                infoz.i_pr_decrypt(bot,chat,sms)
            elif informacion.__contains__ ('listar'):
                infoz.i_listar_(bot,chat,sms)
            elif informacion.__contains__ ('getdb'):
                infoz.i_getdb(bot,chat,sms)
            elif informacion.__contains__ ('view_db'):
                infoz.i_view_db(bot,chat,sms)
            elif informacion.__contains__ ('pr_find'):
                infoz.i_pr_find(bot,chat,sms)
            elif informacion.__contains__ ('add_user'):
                infoz.i_add_user(bot,chat,sms)
            elif informacion.__contains__ ('kick_user'):
                infoz.i_kick_user(bot,chat,sms)
            else:bot.editMessageText(chat_id=chat,message_id=sms.message_id,text='NO HAY AYUDA SOBRE ESE COMANDO ❌\nINTENTA REPORTARLO CON @AresDza')
        except:bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode='HTML',text='Listado de Ayuda para cada Comando 🛰 !!\n\n➖➖➖➖➖➖➖\n<pre>/i pr_decrypt</pre>\n<pre>/i listar</pre>\n<pre>/i getdb</pre>\n<pre>/i view_db</pre>\n<pre>/i pr_find</pre>\n<pre>/i add_user</pre>\n<pre>/i kick_user</pre>\n➖➖➖➖➖➖➖\n\nListado de Ayuda para cada Comando 🛰 !!')

    if '/getdb' in text:
        getUser = user_info
        isadmin = jdb.is_admin(username)
        start.get_db(isadmin,bot,chat,getUser)
        return

    if '/view_db' in text:
        getUser = user_info
        if getUser:
            start.view_db(chat,username,bot)
            return

    if '/add_user' in text:
        getUser = user_info
        isadmin = jdb.is_admin(username)
        if isadmin:
            try:
                user = str(text).split(' ')[1]
                jdb.create_user(user)
                jdb.save()
                msg = '👤 @'+user+' ahora Tiene Acceso al BOT como [USUARIO]'
                bot.sendMessage(chat,msg)
            except:
                bot.sendMessage(chat,'✖️Error en el comando /add_user username✖️')
        elif getUser:
            bot.sendMessage(chat,'✖️No Tiene Permiso✖️')
        return

    if '/kick_user' in text:
        isadmin = jdb.is_admin(username)
        getUser = user_info
        if isadmin:
            try:
                user = str(text).split(' ')[1]
                if user == username:
                    bot.sendMessage(chat,'✖️No Se Puede Banear Usted✖️')
                    return
                jdb.remove(user)
                jdb.save()
                msg = '🚪 @'+user+' ha sido Expulsado 👋🏻'
                bot.sendMessage(chat,msg)
            except:
                bot.sendMessage(chat,'✖️Error en el comando /kick_user username✖️')
        elif getUser:
            bot.sendMessage(chat,'✖️No Tiene Permiso✖️')
        return

# TOKEN
if __name__ == '__main__':
    if dev == 1 :
        administrador = 'AresDza'
        bot_token = '5225993117:AAHjaij0FijHKLHlvCIwPVEdKrQlICApRvo'
        user_id = 1307228755
    else :
        administrador = os.environ.get('administrador')
        bot_token = os.environ.get('bot_token')
        user_id = os.environ.get('user_id')
    bot = telegram.Bot(token=bot_token)
    updater = Updater(token=bot_token, use_context=True)

    # BOT DE LOG: No cambiar, esto se utiliza para Enviar los Errores al Creador del Code para Solucionarlos ....
    botlog_token = '5459923184:AAHQdFUjD18FEgdKoD74Ej0OkYVno4imluY'
    botlog = telegram.Bot(token=botlog_token)
    # BOT DE LOG: No cambiar, esto se utiliza para Enviar los Errores al Creador del Code para Solucionarlos ....

# Despachadores
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=filtrar_text))

# Para Ejecutar el Bot
    updater.start_polling()
    iniciado()
    updater.idle()
