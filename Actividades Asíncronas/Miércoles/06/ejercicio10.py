#Realizado con Python 3.8.10 64-bits en Ubuntu 20.04.2 LTS mediante WSL
#Registro de Contraseña
op='0'
datos=[]
while op!='2':
    print("1) Llenar\n 2) Salir")
    op=input("Elige una opción: ")
    if op=='1':
        usr=input("Ingresar un nombre de usuario: ")
        pwd=input("Ingresar una contraseña mayor a 8 carácteres: ")
        if len(pwd)<9:
            print("Contraseña debil")
        else:
            reg=usr+', '+pwd+'\n'
            datos.append(reg)
    elif op=='2':
        #Si el usuario decide salir del programa
        print("Gracias por usar mi programa")
    else:
        #Si el usuario selecciona una opción no válida
        print("Opción no válida :(")
#Los datos se añaden al archivo pwd.csv
a=open("pwd.csv", "a")
a.writelines(datos)
a.close()
#Se abre el archivo pwd.csv
a=open("pwd.csv", 'r')
contenido=a.read()
a.close()
print(contenido)