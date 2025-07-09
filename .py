import os
import time

def restart_computer():
    os.system("shutdown /r /t 1")

def shutdown_computer():
    os.system("shutdown /s /t 1")

# Apaga la computadora
shutdown_computer()

# Espera 5 segundos antes de encenderla de nuevo
time.sleep(5)

# Enciende la computadora
restart_computer()