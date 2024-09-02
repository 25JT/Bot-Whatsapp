import pywhatkit as kit
from time import sleep

def enviar_mensajes(telefonos, mensaje):
    for telefono in telefonos:
        # Envía el mensaje inmediatamente
        kit.sendwhatmsg_instantly(telefono, mensaje)
        
        # Espera un momento después de enviar el mensaje para evitar problemas de sincronización
        sleep(10)

telefonos = ['+xxxxx']
mensaje = (
    "HOLA COMO ESTAS 🖐️\n"
    "El dia de hoy quiero invitarte a mejorar tus ingresos con YANBAL🤑\n"
    "🤑Escala de ganancia del 25% al 35%\n"
    "🤑Premios por ser nueva\n"
    "🤑Premios por pasar pedido\n"
    "Entregamos a cliente final a nivel nacional\n"
    "Monto mínimo $220.000\n"
    "Escríbeme aquí y te enseñaré"
)

enviar_mensajes(telefonos, mensaje)
