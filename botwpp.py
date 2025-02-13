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

telefonos = ['+573014414701']#agrega los telefonos puedes poner cuantos quieras ejmplo (+5721365412)simpre pon el prefijo seguido del numero
mensaje = (
    "💎*_¡GANA DINERO CON YANBAL! _*💎\n"
    "🚀 ¿Quieres ingresos extras o convertirlo en tu negocio? ¡Es tu momento! Con _Yanbal_ puedes ganar entre un *25%* y un *35%* por tus ventas, además de premios increíbles como *dinero, viajes y autos.* 🚗✈️\n"
    "📢 *Beneficios exclusivos para ti:*\n"
    "✅ Gana desde *$255.000* hasta más de *$2.935.000* en premios.\n"
    "✅ Crédito de hasta *28* días para pagar tu pedido.\n"
    "✅ Entrega a clientes en todo el *país* desde solo *$40.000*.\n"
    "✅ *13* campañas al año, *_¡organiza tus pagos y multiplica tus ganancias!_*\n"
    "📌 Pedido mínimo: $220.000 💰\n"
    "📌 ¡Envía productos directamente a tus clientes y todo suma! 📦\n"
    "📖 Descubre más en nuestra página web:\n"
    "👉 *Yanbal Experiencia*\n(https://proyectoyanbal-b5682.web.app/)\n"
    "✨ Mira el catálogo y empieza a vender ya:\n"
    "📜 *Catálogo Oficial*\n(https://catalogo.yanbal.com/catalogodigital/es/CO/2025/2/oficial/1926325207)  \n"
     "💬 ¡Escríbeme para arrancar esta increíble oportunidad! 🚀 \n"
    )

enviar_mensajes(telefonos, mensaje)

