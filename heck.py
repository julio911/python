#v1: solo subida para probar el git push
import time
import subprocess

print ("hola bienvenido a su fin")
print ("le recomiendo que guarde cualquier archivo")
time.sleep(2)
#v2: introduje un timer para que no se ejecute de inmediato
print("se reiniciara su pc en 15 segundos ")
time.sleep(15)
#v3: comando para reiniciar la pc
subprocess.call("shutdown -r")

