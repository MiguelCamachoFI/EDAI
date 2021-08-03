#Realizado con Python 3.8.10 64-bits en Ubuntu 20.04.2 LTS
#Definir la función name(nombre) para sacar las iniciales del nombre
def name(nombre):
    #Dividir la cadena en una lista
    l = nombre.split()
    new = ""
    #Transversar en la lista
    for i in range(len(l)-0):
        s = l[i]
        #Agrega el primer carácter en minúscula
        new += (s[0].lower())
    #Regresa las iniciales
    return new
#Pregunta al usuario cuál es su nombre
nombre=(input("¿Cuál es tu nombre?: "))
#Saludar al usuario y poner su nombre en mayúsculas y luego en minúsculas
print("Hola ", nombre)
print(nombre.upper())
print(nombre.lower())
#Solicitar su edad
edad=int(input("¿Cuántos años tienes?: "))
#Extraer el tercer carácter de su nombre y concatenarle el triple de su edad dividida entre 2 más su inicial. Ejemplo r40.5m
r=str((edad*3)/2)
#Mostrarle el resultado
print("Su contraseña es: ", nombre[2]+r+name(nombre))