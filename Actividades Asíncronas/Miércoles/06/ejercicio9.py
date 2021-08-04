#Realizado con Python 3.8.10 64-bits en Ubuntu 20.04.2 LTS mediante WSL
#Registro de calificaciones
op='0'
datos=[]
while op!='3':
    print("1) Llenar calificaciones\n 2) Calcular promedio\n 3) Salir")
    op=input("Elige una opción: ")
    if op=='1':
        nom=input("Nombres: ")
        cal=input("Calificación: ")
        reg=nom+','+cal+'\n'
        datos.append(reg)
    elif op=='2':
        cal1=float(input("Ingrese primera calificación: "))
        cal2=float(input("Ingrese segunda calificación: "))
        cal3=float(input("Ingrese tercera calificación: "))
        print("El promedio del grupo es", (cal1+cal2+cal3)/3)
    elif op=='3':
        print("Gracias por usar mi programa")
    else:
        print("Opción no válida :(")
print(datos)
#Guardar las calificaciones de los alumnos en el archivo cal.csv
#a=open("cal.csv", "a")
#a.writelines(datos)
#a.close()

#Abrir el archivo cal.csv
#a=open("cal.csv", 'r')
#contenido=a.read()
#a.close()
#print(contenido)
'''
Marco,9
Lupita,10
Flor,8
'''