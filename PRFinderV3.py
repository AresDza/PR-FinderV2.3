import datetime
import S5Crypto
import time
import socket
import start
import threading
import logging
import time

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

def prfind_e(bot,chat,time_calc,inicio,username,jdb,user_info,text,botlog,listar,administrador):
    pr_find = 0
    rango_min = (text.split('-')[0]).split(' ')[1]
    rango_max = str(int((text.split('-')[1]).split(' ')[0]) + 1)
    ip = str(text).split(' ')[2]
    msg_start = f"🛰<b> Buscando Proxy</b>!!\n<b>🌐 IP :</b> {ip}\n<b>⏯ PUERTOS :</b> {rango_min} - {str(int(rango_max)-1)}\n\n<i>⏳ Por favor espere .....</i>"
    msg_start1 = "\n➖➖➖➖➖➖➖\n\n\n➖➖➖➖➖➖➖"
    msg_succes = f"🛰<b> Proxy Encontrado</b>!!\n<b>🌐 IP :</b> {ip}\n<b>⏯ PUERTOS :</b> {rango_min} - {str(int(rango_max)-1)}\n🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉\n<b>❗️ PROXY ENCONTRADO ❗️</b>"+"\n➖➖➖➖➖➖➖\n"
    msg_succes = f"🛰<b> Proxy Encontrado</b>!!\n<b>🌐 IP :</b> {ip}\n<b>⏯ PUERTOS :</b> {rango_min} - {str(int(rango_max)-1)}\n🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉\n<b>❗️ PROXY ENCONTRADO ❗️</b>"+"\n➖➖➖➖➖➖➖\n"
    error_pr_find = f"🛰 No Hubo Éxito Buscando Proxy!!\n\n❌ IP : {ip}\n\n❌ PUERTOS : {rango_min}-{str(int(rango_max)-1)}"
    succes_pr_find = f"<b>🛰 Finalizada la Búsqueda de Proxy!!\n\n🌐 IP : {ip}\n\n⏯ PUERTOS : {rango_min}-{str(int(rango_max)-1)}</b>"
    lf = msg_start+"\n➖➖➖➖➖➖➖\n"
    rg = "\n➖➖➖➖➖➖➖"
    info = "🛰 Buscando proxy...\n⏯ "+str((int(rango_max)-1)-int(rango_min))+" Puertos"
    listado = '🛰 Proxys Encontrados 🛰\n\n'
    print(info)
    try:
        getUser = user_info
        if getUser:
            getUser['rango_minimo'] = rango_min
            getUser['rango_maximo'] = rango_max
            getUser['ip'] = ip
            jdb.save_data_user(username,getUser)
            jdb.save()
    except:bot.sendMessage(chat,'✖️Error al Guardar IP y Rango de Puertos✖️')
    sms = bot.sendMessage(chat_id=chat,parse_mode="HTML",text=msg_start+msg_start1)
    time.sleep(1.5)
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode="HTML",text=lf+info+rg)
    for port in range(int(rango_min),int(rango_max)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            result = sock.connect_ex((ip,port))
            if result == 0:
                pr_find=1
                info = f'✅ PUERTO : {str(port)}'
                info += f'\n🕰 TT : {str(tt)}'
                if listar == 0: bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode="HTML",text=msg_succes+info+rg)
                if listar == 1: start.porcentaje(rango_max,rango_min,port,info,bot,chat,sms,ip)
                proxy = f'{ip}:{port}'
                proxy_new = S5Crypto.encrypt(f'{proxy}')
                time.sleep(5)
                start.create_historial(username,proxy_new,ip,port)
                sock.close()
                if listar == 0:
                    time_calc.calc_time_s(inicio,proxy_new,chat,sms,bot)
                    bot.pinChatMessage(chat_id=chat, message_id=sms.message_id)
                    break
                if listar == 1:
                    time_calc.calc_time_l(inicio,proxy_new,chat,sms,bot)
            else:
                aho = datetime.datetime.now()
                ahora = datetime.datetime(aho.year, aho.month, aho.day, aho.hour, aho.minute, aho.second)
                tt = ahora - inicio
                info = f'❌ PUERTO : {str(port)}'
                info += f'\n🕰 TT : {str(tt)}'
                start.porcentaje(rango_max,rango_min,port,info,bot,chat,sms,ip)
                sock.close()
        except:
            info = f"<b>IP Inválida ❌ !!\n\nIP: </b><pre>{str(ip)}</pre>"
            bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode="HTML",text=info)
            sock.close()
            break
    try:
        if pr_find==0:
            time_calc.calc_time_e(inicio,chat,sms,bot,error_pr_find)
        if pr_find==1 and listar==1:
            time_calc.calc_time_e(inicio,chat,sms,bot,succes_pr_find)
        else:pass
    except Exception as ex:
        botlog.sendMessage(chat_id=chat,parse_mode='HTML',text=f"<b>🤖 BOT : </b>@{bot.username}\n<b>🔰 DUEÑO : </b>@{administrador}\n\n<pre>{str(ex)}</pre>")
        print(str(ex))
    return

def prfind_p(user_info,bot,chat,username,time_calc,botlog,listar,administrador):
    pr_find=0
    ini = datetime.datetime.now()
    inicio = datetime.datetime(ini.year, ini.month, ini.day, ini.hour, ini.minute, ini.second)
    try:
        getUser = user_info
        if getUser:
            ip = getUser['ip']
            rango_min = getUser['rango_minimo']
            rango_max = getUser['rango_maximo']
    except Exception as ex:
        bot.sendMessage(chat,f'❌ ERROR : {str(ex)}')
        return
    msg_start = f"🛰<b> Buscando Proxy</b>!!\n<b>🌐 IP :</b> {ip}\n<b>⏯ PUERTOS :</b> {rango_min} - {str(int(rango_max)-1)}\n\n<i>⏳ Por favor espere .....</i>"
    msg_start1 = "\n➖➖➖➖➖➖➖\n\n\n➖➖➖➖➖➖➖"
    msg_succes = f"🛰<b> Proxy Encontrado</b>!!\n<b>🌐 IP :</b> {ip}\n<b>⏯ PUERTOS :</b> {rango_min} - {str(int(rango_max)-1)}\n🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉\n<b>❗️ PROXY ENCONTRADO ❗️</b>"+"\n➖➖➖➖➖➖➖\n"
    error_pr_find = f"🛰 No Hubo Éxito Buscando Proxy!!\n\n❌ IP : {ip}\n\n❌ PUERTOS : {rango_min}-{str(int(rango_max)-1)}"
    succes_pr_find = f"<b>🛰 Finalizada la Búsqueda de Proxy!!\n\n🌐 IP : {ip}\n\n⏯ PUERTOS : {rango_min}-{str(int(rango_max)-1)}</b>"
    lf = msg_start+"\n➖➖➖➖➖➖➖\n"
    rg = "\n➖➖➖➖➖➖➖"
    info = "🛰 Buscando proxy...\n⏯ "+str((int(rango_max)-1)-int(rango_min))+" Puertos"
    print(info)
    sms = bot.sendMessage(chat_id=chat,parse_mode="HTML",text=msg_start+msg_start1)
    time.sleep(1.5)
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode="HTML",text=lf+info+rg)
    for port in range(int(rango_min),int(rango_max)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            result = sock.connect_ex((str(ip),port))
            if result == 0:
                pr_find=1
                info = f'✅ PUERTO : {str(port)}'
                info += f'\n🕰 TT : {str(tt)}'
                if listar == 0:
                    bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode="HTML",text=msg_succes+info+rg)
                if listar == 1:
                    start.porcentaje(rango_max,rango_min,port,info,bot,chat,sms,ip)
                proxy = f'{ip}:{port}'
                proxy_new = S5Crypto.encrypt(f'{proxy}')
                time.sleep(5)
                start.create_historial(username,proxy_new,ip,port)
                sock.close()
                if listar == 0:
                    time_calc.calc_time_s(inicio,proxy_new,chat,sms,bot)
                    bot.pinChatMessage(chat_id=chat, message_id=sms.message_id)
                    break
                if listar == 1:
                    time_calc.calc_time_l(inicio,proxy_new,chat,sms,bot)
            else:
                aho = datetime.datetime.now()
                ahora = datetime.datetime(aho.year, aho.month, aho.day, aho.hour, aho.minute, aho.second)
                tt = ahora - inicio
                info = f'❌ PUERTO : {str(port)}'
                info += f'\n🕰 TT : {str(tt)}'
                start.porcentaje(rango_max,rango_min,port,info,bot,chat,sms,ip)
                sock.close()
        except:
            info = f"<b>IP Inválida ❌ !!\n\nIP: </b><pre>{str(ip)}</pre>"
            bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode="HTML",text=info)
            sock.close()
            break
    try:
        if pr_find==0:
            time_calc.calc_time_e(inicio,chat,sms,bot,error_pr_find)
        if pr_find==1 and listar==1:
            time_calc.calc_time_e(inicio,chat,sms,bot,succes_pr_find)
        else:pass
    except Exception as ex:
        botlog.sendMessage(chat_id=chat,parse_mode='HTML',text=f"<b>🤖 BOT : </b>@{bot.username}\n<b>🔰 DUEÑO : </b>@{administrador}\n\n<pre>{str(ex)}</pre>")
        print(str(ex))
    return

lista_errores = ['[Errno 11001] getaddrinfo failed']

def pr_find(id_persona,data,sms,bot,update,pfinal,nhilos,inicio):
    #logging.info("Buscando Puertos abiertos " + str(id_persona))
    userid = update.effective_user.id
    for port in range(id_persona,pfinal,nhilos):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            ip = data
            result = sock.connect_ex((str(ip),port))
            if result == 0:
                info = f"💥Puerto abierto!\n💥Puerto: {port}"
                proxy = f'{ip}:{port}'
                start.create_find(userid,proxy,port)
                print('🔰 '+proxy)
                userid = update.effective_user.id
                ruta = 'pr_finds'
                archivo = open(f'{ruta}/{userid}.txt')
                linea=archivo.readlines()
                aho = datetime.datetime.now()
                ahora = datetime.datetime(aho.year, aho.month, aho.day, aho.hour, aho.minute, aho.second)
                tt = ahora - inicio
                bot.editMessageText(chat_id=update.message.chat.id,parse_mode='HTML',message_id=sms.message_id,text='<b>🛰 Buscando Proxy!!</b>\n<b>🌐 IP : </b>{}\n<b>🔌 PUERTOS ABIERTOS : </b>{}\n<b>🧵 NHilos : </b>{}\n<b>📡 ESCANEANDO PUERTOS!!</b>\n➖➖➖➖➖➖➖\n<b>🕰 TT : </b>{}\n➖➖➖➖➖➖➖'.format(ip,str(len(linea)),str(nhilos),tt))
                sock.close()
            else:
                info = f"Error...Buscando...\nBuscando en el puerto: {str(int(port)+1)}\n"
                sock.close()
        except Exception as ex:
            #print('ERROR: '+str(ex))
            if str(ex) in lista_errores:
                return
            info = f"IP Inválida ❌ !!\n\nIP: {str(ip)}"
            print(info)
            sock.close()
            break
    return

def pr_find_thread(text,bot,update):
    bot = bot
    userid = update.effective_user.id
    ip = str(text).split(' ')[1]
    ini = datetime.datetime.now()
    inicio = datetime.datetime(ini.year, ini.month, ini.day, ini.hour, ini.minute, ini.second)
    aire=' '
    ndpp = 0
    nhilos = 235
    pfinal = 65535
    texto1 = '<b>🛰 Buscando Proxy!!</b>\n<b>🌐 IP : </b>{}\n<b>🔌 PUERTOS ABIERTOS : </b>{}\n<b>🧵 NHilos : </b>{}\n<b>📡 ESCANEANDO PUERTOS!!</b>\n➖➖➖➖➖➖➖\n<b>🕰 TT : </b>{}\n➖➖➖➖➖➖➖'.format(ip,ndpp,str(nhilos),aire)
    sms = bot.sendMessage(chat_id=update.message.chat.id,parse_mode='HTML',text=texto1)

    for i in range(0,nhilos):
        i += 1
        if i != nhilos:
            t = threading.Thread(name='hilo'+str(i),target=pr_find,args=(i, ip, sms, bot, update, pfinal, nhilos, inicio))
            t.start()
        else :
            tf = threading.Thread(name='hilof',target=pr_find,args=(i, ip, sms, bot, update, pfinal, nhilos, inicio))
            tf.start()
    tf.join()
    t.join()
    aho = datetime.datetime.now()
    ahora = datetime.datetime(aho.year, aho.month, aho.day, aho.hour, aho.minute, aho.second)
    tt = ahora - inicio
    try:
        ruta = 'pr_finds'
        archivo = open(f'{ruta}/{userid}.txt')
        linea=archivo.readlines()
        texto2 = '<b>🛰 Buscando Proxy!!</b>\n<b>🌐 IP : </b>{}\n<b>🔌 PUERTOS ABIERTOS : </b>{}\n<b>🧵 NHilos : </b>{}\n<b>🛰 PROCESO FINALIZADO!!</b>\n➖➖➖➖➖➖➖\n<b>🕰  TT : </b>{}\n➖➖➖➖➖➖➖'.format(ip,str(len(linea)),str(nhilos),tt)
        bot.editMessageText(chat_id=update.message.chat.id,parse_mode='HTML',message_id=sms.message_id,text=texto2)
        archivo.close()
        start.view_pr(bot,update,ip)
    except:
        texto2 = '<b>🛰 Buscando Proxy!!</b>\n<b>🌐 IP : </b>{}\n<b>🔌 PUERTOS ABIERTOS : </b>0\n<b>🧵 NHilos : </b>{}\n<b>🛰 PROCESO FINALIZADO!!</b>\n➖➖➖➖➖➖➖\n<b>🕰  TT : </b>{}\n➖➖➖➖➖➖➖'.format(ip,str(nhilos),tt)
        bot.editMessageText(chat_id=update.message.chat.id,parse_mode='HTML',message_id=sms.message_id,text=texto2)