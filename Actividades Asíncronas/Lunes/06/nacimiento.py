#Realizado con Python 3.9.6 64-bits en Fedora 34 Workstation
#Importar la librería datetime
import datetime
#Preguntarle al usuario su edad
edad=int(input("¿Cuántos años tienes?: "))
#Calcula la fecha actual
now=datetime.datetime.now()
#Al año actual restarle la edad del usuario
nacimiento=now.year-edad
#Imprimir su año de nacimiento
print("Su año de nacimiento es: ", nacimiento)