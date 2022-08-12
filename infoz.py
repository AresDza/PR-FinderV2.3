def i_pr_decrypt(bot,chat,sms):
    msg = """👀 El comando /pr_decrypt se usa de la siguiente manera :

👉 /pr_decrypt (proxy)

ℹ️ Esta función desencripta el proxy que le mandes al bot para extraerle el Puerto y el IP. Formato : IP:PORT"""
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,text=msg)

def i_listar_(bot,chat,sms):
    msg = """👀 El comando /listar_(on|off) se usa de la siguiente manera :

👉 /listar_on o /listar_off

ℹ️ Esto alterna entre Lista activa y desactiva para la búsqueda de IP : 
» Si está activa el bot buscará las IP, y al final te dará una lista de IP's válidas y no válidas, diferenciadas por los indicadores ✅ y ❌.
» Si está desactivada el bot buscará las IP, y al encontrar una válida se detendrá la búsqueda y te mostrará sólo esa IP válida.

➕ Este comando viene conjunto con /ip_find"""
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,text=msg)

def i_getdb(bot,chat,sms):
    msg = """👀 El comando /getdb es sólo para el propietario del bot :

👉 /getdb

ℹ️ Obtén la Database del BOT, Incluye, usuarios, IP y Puertos ..."""
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,text=msg)

def i_view_db(bot,chat,sms):
    msg = """👀 El comando /view_db te permite ver tu Historial de Busquedas con éxito 🛰 :

👉 /view_db

ℹ️ Obtén un TXT que contendrá tu Historial de Proxys encontrados del método PROXY  —  IP  —  PUERTO ...

🆙 EXTRAS :
» En caso de no haber encontrado Proxy no podrás acceder a este Historial (Pq aún no ha sido creado 🤷‍♂️)
» Puede ser que ya hayas encontrado proxys, pero los bots al ser actualizados, pierden todos los datos (Incluída la Database)"""
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,text=msg)

def i_pr_find(bot,chat,sms):
    msg = """👀 El comando /pr_find es el que buscará los proxys 🛰 :

USOS :
⚙️ /pr_find - De esta manera el bot buscará en la IP y Puertos Almacenada en la Base de Datos ...
⚙️ /pr_find (ip) - Con este método le pasarás la IP donde buscar al BOT y el Buscará en todos sus puertos ...
⚙️ /pr_find (puerto_inicial-puerto_final) (ip) - De esta manera el bot buscará en la IP y Puertos especificados por ti en el mensaje y luego serán añadidos a tu Base de Datos ...

ℹ️ Utiliza este comando para buscar puertos abiertos que luego se encriptarán y se podrán usar como Proxys ..."""
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,text=msg)

def i_add_user(bot,chat,sms):
    msg = """👀 El comando /add_user es sólo para el propietario del bot :

👉 /add_user (Nombre de Usuario sin el signo de @)

ℹ️ Otorga acceso al Bot a un usuario especificado ..."""
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,text=msg)

def i_kick_user(bot,chat,sms):
    msg = """👀 El comando /kick_user es sólo para el propietario del bot :

👉 /kick_user (Nombre de Usuario sin el signo de @)

ℹ️ Revoca el acceso al Bot a un usuario especificado ..."""
    bot.editMessageText(chat_id=chat,message_id=sms.message_id,text=msg)