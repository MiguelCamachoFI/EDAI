#Realizado con Python 3.9.6 64-bits en Fedora 34 Workstation
#Definir la función name(nombre) para sacar las iniciales del nombre
def name(nombre):
    #Dividir la cadena en una lista
    l = nombre.split()
    new = ""
    #Transversar en la lista
    for i in range(len(l)-0):
        s = l[i]
        #Agrega el primer carácter en mayúscula
        new += (s[0].upper()+'.')
    #Regresa las iniciales
    return new
#Pregunta al usuario cuál es su nombre
nombre=(input("¿Cuál es tu nombre?: "))
#Si el usuario tiene 2 nombres, se une nombres con "*" al inicio
*nombres, apellido1, apellido2 = nombre.split()
#Imprimir el nombre completo separado por nombre(s), apellido paterno y apellido materno
print("Nombre(s) = {nombres},".format(nombres=" ".join(nombres)), "Apellido Paterno = {apellido1},".format(apellido1=apellido1), "Apellido Materno = {apellido2}".format(apellido2=apellido2))
#Imprime las iniciales separadas por puntos
print("Las iniciales de tu nombre son: ", name(nombre))