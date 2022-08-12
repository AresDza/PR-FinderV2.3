import socket
import S5Crypto
import os
import time
from JDatabase import JsonDatabase
import JDatabase as jdb

def create_historial(username,proxy_new,ip,port):
    ruta = 'historial'
    archivo = f'{ruta}/{username}.txt'
    try:
        if not os.path.exists(ruta):os.makedirs(ruta)
        if not os.path.exists(ruta):open(archivo, 'w')
        write='PROXY : '+str(proxy_new)
        write+=' -- IP : '+str(ip)
        write+=' -- PUERTO : '+str(port)+'\n'
        with open(archivo, 'a') as db :db.write(write)
    except Exception as ex:print(str(ex))

def create_find(userid,proxy,port):
    proxy_new = S5Crypto.encrypt(f'{proxy}')
    ruta = 'pr_finds'
    archivo = f'{ruta}/{userid}.txt'
    try:
        if not os.path.exists(ruta):os.makedirs(ruta)
        if not os.path.exists(ruta):open(archivo, 'w')
        write='> PROXY : '+str(proxy_new)
        write+='\n> PUERTO : '+str(port)+'\n\n'
        with open(archivo, 'a') as db :db.write(write)
    except Exception as ex:print(str(ex))

def create_find_white(userid):
    ruta = 'pr_finds'
    archivo = f'{ruta}/{userid}.txt'
    try:
        if not os.path.exists(ruta):os.makedirs(ruta)
        if not os.path.exists(ruta):open(archivo, 'w')
    except Exception as ex:print(str(ex))

def view_db(chat,username,bot):
    ruta = 'historial'
    archivo = f'{ruta}/{username}.txt'
    try:
        with open(archivo, 'rb') as db, open("PR-FinderV2-Cuadrado.jpg", "rb") as miniatura:
            bot.sendChatAction(chat,"upload_document")
            bot.sendDocument(chat_id=chat, parse_mode='HTML', document=db, caption='📋 Historial 📋\n🧬 User : @'+username, thumb=miniatura)
    except:
        bot.sendMessage(chat,'😬 Ups ....\n» Todavía no tienes un Historial de Proxys — Puertos — IP\no :\n» El bot se reinició y se borraron todos los datos (historial,database)')

def view_pr(bot,update,ip):
    userid = update.effective_user.id
    ruta = 'pr_finds'
    archivo = f'{ruta}/{userid}.txt'
    file = open(f'{ruta}/{userid}.txt', 'r')
    #try:
    #    with open(archivo, 'rb') as db, open("PR-FinderV2-Cuadrado.jpg", "rb") as miniatura:
    #        bot.sendChatAction(update.message.chat.id,"upload_document")
    #        linea=file.readlines()
    #        total_lines=len(linea)
    #        file.close()
    #        bot.sendDocument(chat_id=update.message.chat.id, parse_mode='HTML', document=db, caption='<b>📋 PUERTOS ABIERTOS: </b>{}'.format(total_lines), thumb=miniatura)
    #    os.remove(archivo)
    try:
        data = file.read()
        bot.sendMessage(chat_id=update.message.chat.id,text='🥳 SCAN A IP FINALIZADO 🥳\n🛰️ IP : '+ip+'\n\n'+data)
        file.close()
        os.remove(archivo)
    except Exception as ex:
        bot.sendMessage(update.message.chat.id,'😬 Ups ....\n» '+str(ex))

def get_db(isadmin,bot,chat,getUser):
    if isadmin:
        with open("database.jdb", "rb") as db, open("PR-FinderV2-Cuadrado.jpg", "rb") as miniatura:
            bot.sendChatAction(chat,"upload_document")
            bot.sendDocument(chat_id=chat, parse_mode="HTML", document=db, caption='🛰 BASE DE DATOS 🛰', thumb=miniatura)
    elif getUser:
        bot.sendMessage(chat,'✖️No Tiene Permiso✖️')

def start_i(username,userid,userdata,isadmin,listar):
    msg = 'Bienvenido al BOT PR-Finder V2 🛰\n'
    msg+= 'PR-FinderV2.3🛰 | Code by : @AresDza\n\n'
    if username != 'None' or username != 'none':
        msg+= '🧬 USERNAME : @' + str(username)+'\n'
    msg+= '🆔 ID : <pre>' + str(userid)+'</pre>\n\n'
    msg+= '🛰 IP : ' + str(userdata['ip'])+'\n'
    listado = '🗒 LISTAR : SI'
    if listar:listado = '🗒 LISTAR : NO'
    msg+= listado + '\n'
    msg+= '▶️ PUERTO INICIAL : ' + str(userdata['rango_minimo'])+'\n'
    msg+= '⏸ PUERTO FINAL : ' + str(userdata['rango_maximo'])+'\n\n'
    stat = '👤 ‖USER‖ 👤'
    if isadmin:stat = '👑 ‖OWNER‖ 👑'
    msg+= stat + '\n'
    return msg

def porcentaje(rango_max,rango_min,port,info,bot,chat,sms,ip):
    maxim = int(rango_max) - int(rango_min)
    actual = (int(port)+1) - int(rango_min)
    porcent = actual / maxim
    porcent *= 100
    porcent = int(str(porcent).split('.')[0])
    if porcent in range(0,10):
        n = '🟩'*0
        b = '⬛️'*10
    elif porcent in range(10,20):
        n = '🟩'*1
        b = '⬛️'*9
    elif porcent in range(20,30):
        n = '🟩'*2
        b = '⬛️'*8
    elif porcent in range(30,40):
        n = '🟩'*3
        b = '⬛️'*7
    elif porcent in range(40,50):
        n = '🟩'*4
        b = '⬛️'*6
    elif porcent in range(50,60):
        n = '🟩'*5
        b = '⬛️'*5
    elif porcent in range(60,70):
        n = '🟩'*6
        b = '⬛️'*4
    elif porcent in range(70,80):
        n = '🟩'*7
        b = '⬛️'*3
    elif porcent in range(80,90):
        n = '🟩'*8
        b = '⬛️'*2
    elif porcent in range(90,100):
        n = '🟩'*9
        b = '⬛️'*1
    elif porcent == 100:
        n = '🟩'*10
        b = '⬛️'*0

    if porcent != 100 :porcente = '☑️'
    else :porcente = '✅'
    progress = n+b

    msg = '🛰 <b>Buscando Proxy</b>!!\n<b>🌐 IP : </b>'+str(ip)+'\n'
    msg+='<b>⏯ PUERTOS : </b>'+str(rango_min)+'-'+str(int(rango_max)-1)
    msg+='\n'+progress
    msg+='\n'+porcente+'<b> PORCIENTO : </b>'+str(porcent)+'%\n➖➖➖➖➖➖➖\n'
    msg+=info+'\n➖➖➖➖➖➖➖'
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,parse_mode="HTML",text=msg)