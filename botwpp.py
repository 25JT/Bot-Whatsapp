import pywhatkit as kit
import pyautogui
import time

# Función para leer números desde un archivo de texto
def cargar_telefonos(nombre_archivo="telefonos.txt"):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            telefonos = [line.strip() for line in file if line.strip()]
        return telefonos
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo telefonos.txt. Asegúrate de crearlo y agregar números.")
        time.sleep(10)
        return []

# Mensaje de WhatsApp
mensaje = """💎 *_¡GANA DINERO CON YANBAL!_* 💎  

🚀 ¿Quieres ingresos extras o convertirlo en tu negocio? ¡Es tu momento! Con _Yanbal_ puedes ganar entre un *25%* y un *35%* por tus ventas, además de premios increíbles como *dinero, viajes y autos.* 🚗✈️  

📢 *Beneficios exclusivos para ti:*  
✅ Gana desde *$255.000* hasta más de *$2.935.000* en premios.  
✅ Crédito de hasta *28 días* para pagar tu pedido.  
✅ Entrega a clientes en todo el *país* desde solo *$40.000*.  
✅ *13 campañas* al año, *_¡organiza tus pagos y multiplica tus ganancias!_*  

📌 Pedido mínimo: $220.000 💰  
📌 ¡Envía productos directamente a tus clientes y todo suma! 📦  

📖 Descubre más en nuestra página web:  
👉 *Yanbal Experiencia* (https://proyectoyanbal-b5682.web.app/)  

✨ Mira el catálogo y empieza a vender ya:  
📜 *Catálogo Oficial* (https://catalogo.yanbal.com/catalogodigital/es/CO/2025/2/oficial/1926325207)  

💬 ¡Escríbeme para arrancar esta increíble oportunidad! 🚀"""

# Función para enviar mensajes
def enviar_mensajes(telefonos, mensaje):
    total_enviados = 0
    for telefono in telefonos:
        try:
            print(f"📲 Enviando mensaje a {telefono}...")
            kit.sendwhatmsg_instantly(telefono, mensaje)  # Enviar mensaje
            
            time.sleep(10)  # Esperar para evitar bloqueos (ajustar si es necesario)
            pyautogui.hotkey("ctrl", "w")  # Cerrar pestaña de WhatsApp
            
            total_enviados += 1  # Contador de mensajes enviados
            
        except Exception as e:
            print(f"❌ Error al enviar mensaje a {telefono}: {e}")
            time.sleep(5)
    
    # Mensaje final indicando cuántos mensajes se enviaron correctamente
   
    pyautogui.alert(text=f"✅ Proceso finalizado. Se enviaron {total_enviados} mensajes exitosamente.",title='BOT WPP 📲', button='OK')

# Cargar teléfonos y enviar mensajes
telefonos = cargar_telefonos()
if telefonos:
    enviar_mensajes(telefonos, mensaje)
else:
    print("⚠️ No hay números de teléfono para enviar mensajes.")
    time.sleep(10)
