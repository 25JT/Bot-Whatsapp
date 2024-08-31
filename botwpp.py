import pyautogui
import webbrowser
from time import sleep

def enviar_mensajes(telefonos, mensaje, repeticiones=1):
    for telefono in telefonos:
        url = f'https://web.whatsapp.com/send?phone={telefono}'
        webbrowser.open(url)
        sleep(10)  # Espera a que se cargue la página de WhatsApp Web
        
        for _ in range(repeticiones):
            pyautogui.typewrite(mensaje)
            pyautogui.press('enter')
        
        sleep(5)  # Espera un poco antes de cerrar la pestaña
        pyautogui.hotkey('ctrl', 'w')  # Cierra la pestaña actual

telefonos = ['Number1', 'Number2','....']
mensaje = "TEXT  HERE"

enviar_mensajes(telefonos, mensaje, repeticiones=1)
