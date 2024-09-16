import pywhatkit as kit
import pyautogui
from time import sleep

def enviar_mensajes(telefonos, mensaje):
    for telefono in telefonos:
        # Envía el mensaje inmediatamente
        kit.sendwhatmsg_instantly(telefono, mensaje)
        
        # Espera un momento después de enviar el mensaje para evitar problemas de sincronización
        sleep(5)
        pyautogui.hotkey('ctrl', 'w')

telefonos = ['+xxxxxx','+xxxxxx']
mensaje = (
    "*_¡Hola ¿Cómo estás?_* 🖐️\n"
    "Hoy quiero invitarte a descubrir una oportunidad increíble para aumentar tus ingresos con *YANBAL*💸\n"
    "🔝 *Gana* entre un *25%* y un *35%*, y si te lo propones, ¡puedes llegar a ganar *autos* y *viajes*! 🚗✈️\n"
    "🎁*Premios* exclusivos para nuevas consultoras.\n"
    "📦*Bonificaciones por cada pedido realizado.*\n"
    "🌍*_Entregamos a cliente final a nivel nacional_*\n"
    "con un monto mínimo $220.000 y entrega al cliente desde $40.000\n"
    "¡Escríbeme aquí y te enseño cómo empezar! 💬"
)

enviar_mensajes(telefonos, mensaje)
