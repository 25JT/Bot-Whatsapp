import pywhatkit as kit
import pyautogui
from time import sleep

def enviar_mensajes(telefonos, mensaje):
    for telefono in telefonos:
        # Envía el mensaje inmediatamente
        kit.sendwhatmsg_instantly(telefono, mensaje)
        
        # Espera un momento después de enviar el mensaje para evitar problemas de sincronización
        sleep(10)#aqui puedes cambiar el tiempo que domore en esperar para enviar el msj esta puesto en seg 
        pyautogui.hotkey('ctrl', 'w')#cierra la pestaña despues de enviar el msj

telefonos = ['+xxxxxx','+xxxxxx']#agrega los telefonos puedes poner cuantos quieras ejmplo (+5721365412)simpre pon el prefijo seguido del numero
mensaje = (
    "*_¡Hola! ¿Te gustaría ganar más dinero?_* 🖐️\n"
    "Hoy tienes la oportunidad perfecta para comenzar a generar ingresos extra con *YANBAL* 💸\n"
    "🔝 *Gana* entre un *25%* y un *35%*, y si te lo propones, ¡puedes llegar a ganar *autos* y *viajes*! 🚗✈️\n"
    "🎁*Premios* exclusivos para nuevas consultoras.\n"
    "📦*Bonificaciones por cada pedido realizado.*\n"
    "🌍*_Entregamos a cliente final a nivel nacional_*\n"
    "con un monto mínimo $220.000 y entrega al cliente desde $40.000\n"
    "¡Escríbeme para comenzar esta aventura juntas!! 💬"
)

enviar_mensajes(telefonos, mensaje)
